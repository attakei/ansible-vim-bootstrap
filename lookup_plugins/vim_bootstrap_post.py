from ansible.plugins.lookup import LookupBase


QUERY_TERMS = (
    "langs",
)


class LookupModule(LookupBase):
    def run(self, terms, **kwargs):
        query = []
        for idx, key in enumerate(QUERY_TERMS):
            for val in terms[idx]:
                query.append((key, val))
        return query
