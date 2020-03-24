#!/usr/bin/env python3

import awsops
import parsing
import config

def main():
    parser = parsing.Parsing()
    args = parser.args_parser()
    aws = awsops.AwsOperations(args)
    route_table_id = aws.create_route_table()
    aws.create_tags(route_table_id, config.PUBLIC_TAG)
    aws.add_internet_gateway_route(route_table_id, config.DESTINATION)
    subnet_id = aws.get_subnet_id(config.PUBLIC_TAG)
    aws.associate_route_table(route_table_id, subnet_id)
    private_route_table_id = aws.create_route_table()
    aws.create_tags(private_route_table_id, config.PRIVATE_TAG)
    private_subnet_id = aws.get_subnet_id(config.PRIVATE_TAG)
    aws.associate_route_table(private_route_table_id, private_subnet_id)
    aws.add_nat_gateway_route(private_route_table_id, config.DESTINATION, config.CIDR)
    # create private route table
    # create tags for the private route table
    # get private subnet id
    # create nat gateway route
    # associate the private subnet with the private route table

if __name__ == '__main__':
    main()
