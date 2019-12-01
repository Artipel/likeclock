import json
import requests
import datagramer
import sched
import time


def validate_config(config_file):
    missing = []
    if 'url' not in config_file:
        missing.append('url')
    if 'interval' not in config_file:
        missing.append('interval')
    if 'path' not in config_file:
        missing.append('path')
    return missing


def load_config(config_path):
    try:
        f = open(config_path, "r")
        config = json.load(f)
    except json.decoder.JSONDecodeError:
        print("Error in configuration file syntax")
        raise Exception(102)
    except FileNotFoundError:
        print("Configuration file not found")
        raise Exception(101)
    content_missing = validate_config(config)
    if len(content_missing) > 0:
        print("Error in configuration file content. Missing elements: " + str(content_missing))
        raise Exception(103)
    return config


def extract_item(object, path):
    try:
        node = object
        for step in path:
            node = node[step]
    except Exception:
        raise Exception(104)
    return node


def make_request(url):
    try:
        r = requests.request('GET', url)
    except Exception as error:
        print(error)
        print('Internet connection error')
        raise Exception(100)
    return r


def routine_iteration(config, sch):
    try:
        r = make_request(config['url'])
        number = extract_item(r.json(), config['path'])
        send_number(number)
        sch.enter(config['interval'], 1, routine_iteration, kwargs={'config': config, 'sch': sch})
    except Exception as exc:
        print('Error occured. Error no.: ' + str(exc))
        datagramer.show_error(exc)


def send_number(number):
    try:
        datagramer.send(number)
        print('Sending number to display: ' + str(number))
    except Exception as error:
        print(error)
        print('Error while sending data over serial')
        raise Exception(105)


def main():
    try:
        config = load_config('/boot/config.json')
        r = make_request(config['url'])
        number = extract_item(r.json(), config['path'])
        send_number(number)
        try:
            sch = sched.scheduler(time.time, time.sleep)
            sch.enter(5, 1, routine_iteration, kwargs={'config': config, 'sch': sch})
            sch.run()
        except Exception as error:
            print(error)
            print('Scheduler exception')
            raise Exception(110)
    except Exception as exc:
        print('Error occured. Error no.: ' + str(exc))
        datagramer.show_error(exc)


if __name__ == '__main__':
    main()








