from ansible.plugins.lookup import LookupBase


QUERY_TERM_RULES = (
    (list, "langs"),
    (list, "frameworks"),
    (str, "theme"),
    (str, "editor"),
)


class LookupModule(LookupBase):
    def run(self, terms, **kwargs):
        query = []
        for idx, rule in enumerate(QUERY_TERM_RULES):
            if rule[0] == str:
                query.append((rule[1], terms[idx]))
                continue
            for val in terms[idx]:
                query.append((rule[1], val))
        return query
