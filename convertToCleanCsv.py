import csv

with open("reports-clean.csv", mode="w") as clean_data:
    clean_writer = csv.writer(
        clean_data, delimiter=",", quotechar='"', quoting=csv.QUOTE_NONNUMERIC
    )

    # Write CSV Column Names
    clean_writer.writerow(
        [
            "incident_datetime",
            "incident_id",
            "report_type_code",
            "report_type_description",
            "filed_online",
            "incident_code",
            "incident_category",
            "incident_subcategory",
            "incident_description",
            "resolution",
            "intersection",
            "police_district",
            "analysis_neighborhood",
        ]
    )

    with open("reports-2018-onwards.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=";")
        line_count = 0

        for row in csv_reader:
            line_count += 1
            if line_count > 1:
                clean_writer.writerow(
                    [
                        row[0],
                        row[7],
                        row[10],
                        row[11],
                        row[12],
                        row[13],
                        row[14],
                        row[15],
                        row[16],
                        row[17],
                        row[18],
                        row[20],
                        row[21],
                    ]
                )

        print(f"Processed {line_count} lines.")
