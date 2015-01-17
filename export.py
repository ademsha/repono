# -*- coding: utf-8 -*-
import datetime

from export.tocsv import ExportToCSV


if __name__ == "__main__":

    print "Exporting to CSV started // " + str(datetime.datetime.utcnow())

    ExportToCSV().export_all()

    print "Exporting to CSV finished // " + str(datetime.datetime.utcnow())
