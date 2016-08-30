# -*- coding: utf-8 -*-

"""
B2SAFE internal service operations
served as HTTP REST API endpoints.
"""

from __future__ import absolute_import

from commons.logs import get_logger
from commons.services.uuid import getUUID
from ...base import ExtendedApiResource
from ... import decorators as decorate
from ....auth import authentication
from ....confs import config

logger = get_logger(__name__)


class MetadataObject(ExtendedApiResource):

    # @authentication.authorization_required(config.ROLE_INTERNAL)
    # @decorate.apimethod
    # def get(self):
    #     return "Hello world"

    @authentication.authorization_required(config.ROLE_INTERNAL)
    # @decorate.add_endpoint_parameter("user", required=True)
    # @decorate.add_endpoint_parameter("location", required=True)
    @decorate.apimethod
    def post(self):
        """ Register a UUID """

        # Create graph object
        graph = self.global_get_service('neo4j')
        icom = self.global_get_service('irods')

        #######################
        #######################
# // TO FIX: request a 'user' parameter
        # User
        myuser = None
        userobj = self.get_current_user()
        irodsusers = userobj.associated.search(default_user=True)
        if len(irodsusers) < 1:
            # associate with guest user?
            class myuser(object):
                username = icom.get_default_user()
        else:
            myuser = irodsusers.pop()
        myuserobj = None
        try:
            myuserobj = graph.IrodsUser.nodes.get(username=myuser.username)
        except graph.IrodsUser.DoesNotExist:
            return self.response(errors={
                'iRODS user':
                    'no valid account associated on the iRODS server'})
        #######################
        #######################

        #######################
        # Create UUID
        myid = getUUID()
# // TO FIX: request a 'location' parameter
        mylocation = 'noprotocol:///%s/%s/TOBEDEFINED' % (myuser, myid)
        dobj = graph.DataObject(id=myid, location=mylocation)
        dobj.save()

        #######################
        # Link the obj
        dobj.owned.connect(myuserobj)

        #######################
        # Return the UUID
        return dobj.id