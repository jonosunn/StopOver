import os

from django.test.runner import DiscoverRunner

class HerokuDiscoverRunner(DiscoverRunner):
    def setup_databases(self, **kwargs):
        if not os.environ.get('IS_HEROKU_TEST'):
            raise ValueError(
                "The IS_HEROKU_TEST env variable must be set to enable this.  WARNING:  "
                "This test runner will wipe all tables in the database it targets!")
        self.keepdb = True
        return super(HerokuDiscoverRunner, self).setup_databases(**kwargs)

    def _wipe_tables(self, connection):
        with connection.cursor() as cursor:
            cursor.execute(
                """
                    DROP SCHEMA public CASCADE;
                    CREATE SCHEMA public;
                    GRANT ALL ON SCHEMA public TO postgres;
                    GRANT ALL ON SCHEMA public TO public;
                    COMMENT ON SCHEMA public IS 'standard public schema';
                """
            )

    def teardown_databases(self, old_config, **kwargs):
        self.keepdb = True
        for connection, old_name, destroy in old_config:
            if destroy:
                self._wipe_tables(connection)
        super(HerokuDiscoverRunner, self).teardown_databases(old_config, **kwargs)
