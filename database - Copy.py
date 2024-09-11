import os
import psycopg2

# Database connection configuration for PostgreSQL
db_config_pg = {
    'host': 'localhost',
    'user': 'postgres',
    'password': 'sadaf',
    'database': 'postgres',
}

# Establish a connection to the PostgreSQL database
conn_pg = psycopg2.connect(**db_config_pg)

# Function to insert data into PostgreSQL table
def insert_data_pg(student_name, image_url, image_features):
    insert_query_pg = (
        "INSERT INTO {} (student_name, image_url, image_features) "
        "VALUES (%s, %s, %s) RETURNING student_id"
    ).format(table_name_pg)

    values_pg = (student_name, image_url, image_features)

    cursor_pg.execute(insert_query_pg, values_pg)
    conn_pg.commit()

    # Fetch the generated student_id
    student_id = cursor_pg.fetchone()[0]

    return student_id

# Commit changes to the PostgreSQL database
conn_pg.commit()

# Output folder containing images and encoding of images features
output_folder = "D:\internproject\output_folder"

# Count to process only the first 8 files
count = 0

# Iterate over the files in the output folder
for filename in os.listdir(output_folder):
    if count >= 8:
        break

    if filename.endswith(".jpg"):
        print(filename)
        image_path = os.path.join(output_folder, filename)
        student_name = filename.split('.')[0]
        student_id = int(filename.split('_')[0])

        # Check if corresponding features file exists
        features_path = os.path.join(output_folder, f"{student_name}.txt")
        print(features_path)
        if os.path.exists(features_path):
            # Read image features from file
            with open(features_path, 'r') as features_file:
                # Assuming the file contains a single line with space-separated numeric values
                image_features = list(map(float, features_file.read().split()))

            # Construct image URL based on the local path
            base_path = "D:/internproject/output1_folder/"
            image_url = f"{base_path}{filename}"

            # Insert data into PostgreSQL table and get the generated student_id
            student_id = insert_data_pg(student_name, image_url, image_features)

            print(f"Inserted record with student_id: {student_id}")

        count += 1

# Commit changes and close the PostgreSQL connection
conn_pg.commit()
conn_pg.close()
