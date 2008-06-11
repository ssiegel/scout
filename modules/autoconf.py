import scout

class ScoutModule(object):

    name = "autoconf"
    desc = "Search for autoconf macros inside the m4 files."

    @classmethod
    def main(cls):
        """ a main method """

        p = scout.Parser(cls.name)
        p.add_repos_from_datadir()
        if not p.parse():
            return None

        print p.options
        print p.args
        return None
