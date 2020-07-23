import csv
import time
import argparse
from mpu6050 import mpu6050


def data_writer(path='accelerometer_data.csv', load_calibration=True):
    """Data writer. Its add the index frame""
        points = list or array with x, y, z values
        load_calibration = 'accel_calibration.csv' must be defined"""
    sensor = mpu6050(0x68)
    sensor.set_accel_range()
    fieldnames = ['frame', 'x', 'y', 'z']
    with open(path, 'w') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writerow({fieldname: fieldname for fieldname in fieldnames})
    if load_calibration:
        sensor.set_calibrate_accel()
    start_time = time.time()
    print('Tomando muestras')
    while True:
        points = sensor.get_accel_data()
        #print('x: {}, y: {}, z: {}, t:{}'.format(points['x'], points['y'], points['z'], time.time()-start_time))
        with open(path, 'a') as csv_file:
            points['frame'] = time.time()-start_time
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writerow(points)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='data_writer',
                                        usage='%(prog)s [options] path',
                                        description='save mpu6050 lectures')
    parser.add_argument('--cali', action='store_true', required=False)
    parser.add_argument('--raw', action='store_true', required = False)
    parser.add_argument('--path', action='store', type=str, required=False)
    args = parser.parse_args()
    if args.cali:
        data_writer(path='accel_calibration.csv', load_calibration=False)
        print('corriendo calibración se guardara en accel_calibration.csv')
    else:
        if args.raw:
            if args.path:
                data_writer(path=args.path, load_calibration=False)
            else:
                data_writer(load_calibration=False)
        else:
            if args.path:
                data_writer(path=args.path)
            else:
                data_writer()

