# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUPolicyDecisionsFetcher(NURESTFetcher):
    """ PolicyDecision fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUPolicyDecision
        return NUPolicyDecision