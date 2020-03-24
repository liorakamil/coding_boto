#!/usr/bin/env python3
"""
This module creates public and private subnet.
"""

import awsops
import parsing
import config


def main():
    """
    This function create a private and a public subnet
    """
    parser = parsing.Parsing()
    args = parser.args_parser()
    aws = awsops.AwsOperations(args)
    public_cidr = config.MAPPING[config.PUBLIC_TAG]
    subnet_id = aws.create_subnet(public_cidr)
    aws.create_tags(subnet_id, config.PUBLIC_TAG)
    private_cidr = config.MAPPING[config.PRIVATE_TAG]
    private_subnet_id = aws.create_subnet(private_cidr)
    aws.create_tags(private_subnet_id, config.PRIVATE_TAG)
    # get private subnet cidr
    # create private subnet
    # tag the private subnet


if __name__ == '__main__':
    main()