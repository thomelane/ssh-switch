import argparse
import boto3
import os


def switch_instance(action, instance_id):
    ec2 = boto3.resource('ec2')
    instance = ec2.Instance(instance_id)
    if action == "on":
        instance.start()
    elif action == "off":
        instance.stop()
    else:
        raise ValueError("Action must be 'on' or 'off'.")
    

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("action")
    parser.add_argument("host")
    args = parser.parse_args()
    return args


def find_instance_id(host):
    correct_host = None
    instance_id = None
    with open(os.path.expanduser('~/.ssh/config'), 'r') as openfile:
        for line in openfile:
            line = line.strip()
            if line.startswith('Host '):
                correct_host = line == 'Host {}'.format(host)
                continue
            if correct_host:
                if line.startswith('# InstanceId '):
                    instance_id = line[len('# InstanceId '):]
    if not instance_id:
        raise Exception("Couldn't find Instance ID for {} in ~/.ssh/config.".format(host))
    return instance_id


def main():
    args = parse_args()
    instance_id = find_instance_id(args.host)
    switch_instance(args.action, instance_id)
