# Test Script
# To run test, use the command under the pipeline folder
# DB_USER=postgres DB_PASSWORD=secret DB_HOST=localhost TOKEN=<token> python3 -m unittest scraper/test.py -v in the scraper folder

import sys
from .PSQL import *
from .GitHubQuery import *
import unittest
import json
import urllib
import datetime

def make_orderer():
    order = {}

    def ordered(f):
        order[f.__name__] = len(order)
        return f

    def compare(a, b):
        return [1, -1][order[a] < order[b]]

    return ordered, compare

ordered, compare = make_orderer()
unittest.defaultTestLoader.sortTestMethodsUsing = compare

class TestMyClass(unittest.TestCase):


    @ordered
    def test_runQueryOnce(self):
        monthStr = "created:2020-01-01..2020-02-01"
        cursor = ""
        for i in [1,10,100]:
            result = runQueryOnce(i, monthStr, cursor)
            json_obj = None
            try:
                json_obj = json.load(result)
                print(json_obj)
                self.assertIsNotNone(json_obj)
            except:
                self.assertIsNone(json_obj)


    @ordered
    def test_connectToDB(self):
        db = connectToDB()
        self.assertIsNotNone(db)


    @ordered
    def test_insertToApplication(self):
        db = connectToDB()
        url = "www.pkgpkr.com"
        followers = 314
        appName = "pkgpkr"
        myHash = hash(appName)
        id = insertToApplication(db,url,followers,appName,myHash)
        self.assertIsInstance(id, int)
        cur = db.cursor()
        cur.execute(
            "SELECT name FROM applications WHERE id = %s;" % (id)
        )
        application_name = cur.fetchone()[0]
        self.assertEqual(application_name, appName)


    @ordered
    def test_insertToPackages(self):
        db = connectToDB()
        name = "myPkg"
        id = insertToPackages(db, name)
        self.assertIsInstance(id, int)
        cur = db.cursor()
        cur.execute(
            "SELECT name FROM packages WHERE id = %s;" % (id)
        )
        package_name = cur.fetchone()[0]
        self.assertEqual(package_name, name)


    @ordered
    def test_updatePackageMetadata(self):
        db = connectToDB()
        name = "myPkg"
        downloads_last_month = 200
        categories = ["critical", ",,comma", "\\{braces\\}", "\'quoted\""]
        modified = datetime.datetime.now()

        # Insert package into the table
        id = insertToPackages(db, name)
        self.assertIsInstance(id, int)

        # Ensure that the modified field is None
        cur = db.cursor()
        cur.execute(
            "SELECT modified FROM packages WHERE id = %s;" % (id)
        )
        modified_date = cur.fetchone()[0]
        self.assertIsNone(modified_date)

        # Update metadata in the table
        updatePackageMetadata(db, name, downloads_last_month, categories, modified)

        # Ensure that the modified field is now not None
        cur.execute(
            "SELECT modified FROM packages WHERE id = %s;" % (id)
        )
        modified_date = cur.fetchone()[0]
        self.assertIsNotNone(modified_date)

        # Upsert the same package into the table again
        id = insertToPackages(db, name)
        self.assertIsInstance(id, int)

        # Ensure that the modified field is still not None
        cur.execute(
            "SELECT modified FROM packages WHERE id = %s;" % (id)
        )
        modified_date = cur.fetchone()[0]
        self.assertIsNotNone(modified_date)


    @ordered
    def test_insertToDependencies(self):
        db = connectToDB()
        url = "www.pkgpkr.com"
        followers = 314
        appName = "pkgpkr"
        myHash = hash(appName)
        application_id = insertToApplication(db,url,followers,appName,myHash)
        name = "myPkg"
        package_id = insertToPackages(db, name)
        insertToDependencies(db, application_id, package_id)
        cur = db.cursor()
        cur.execute(
            "SELECT * FROM dependencies WHERE application_id = %s AND package_id = %s;"
            % (application_id, package_id)
        )
        result = cur.fetchall()
        self.assertEqual(result, [(application_id, package_id)])

if __name__ == "__main__":
    unittest.main()
