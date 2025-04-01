import csv
from your_app import db
from your_app.models import Peak

with open('peaks.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        peak = Peak(
            name=row['name'],
            latitude=float(row['latitude']),
            longitude=float(row['longitude']),
            elevation=int(row['elevation']),
            description=row['description'],
            photo_url=row['photo_url'],
        )
        db.session.add(peak)
db.session.commit()

