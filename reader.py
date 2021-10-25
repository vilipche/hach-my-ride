# script used to create a csv file from all the json data.


import json
from typing import TextIO

FILES = [
    './vehiclePosition01.json',
    './vehiclePosition02.json',
    './vehiclePosition03.json',
    './vehiclePosition04.json',
    './vehiclePosition05.json',
    './vehiclePosition06.json',
    './vehiclePosition07.json',
    './vehiclePosition08.json',
    './vehiclePosition09.json',
    './vehiclePosition10.json',
    './vehiclePosition11.json',
    './vehiclePosition12.json',
    './vehiclePosition13.json'
]


def convert_json_into_csv(csv_file: TextIO, json_path: str) -> None:
    file = open(json_path, 'r')
    data = json.load(file)['data']
    for time in data:
        timestamp = int(time['time'])
        responses = time['Responses']
        for response in responses:
            if response is None:
                continue
            lines = response['lines']
            for line in lines:
                line_id = line['lineId']
                for vehiclePosition in line['vehiclePositions']:
                    csv_file.write(
                        f"{timestamp},"
                        f"{line_id},"
                        f"{vehiclePosition['directionId']},"
                        f"{vehiclePosition['distanceFromPoint']},"
                        f"{vehiclePosition['pointId']}\n")


def create_csv_from_json(json_path: str) -> None:
    csv_path = json_path.replace('.json', '.csv')
    csv_file = open(csv_path, 'w')
    csv_file.write('Timestamp,LineId,DirectionId,DistanceFromPoint,PointId\n')
    convert_json_into_csv(csv_file, json_path)


def convert_json_files() -> None:
    for file in FILES:
        print(f'Start converting file {file}')
        create_csv_from_json(file)
        print(f'Finish converting file {file}')


def convert_json_files_into_single_csv() -> None:
    csv_file = open('vehiclePositions.csv', 'w')
    csv_file.write('Timestamp,LineId,DirectionId,DistanceFromPoint,PointId\n')
    for path in FILES:
        print(f'Start converting file {path}')
        convert_json_into_csv(csv_file, path)
        print(f'Finish converting file {path}')


def main() -> None:
    convert_json_files_into_single_csv()


if __name__ == '__main__':
    main()
