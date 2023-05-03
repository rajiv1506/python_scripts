import boto3



client = boto3.client('ec2', region_name='us-east-1' ,aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)


# retrieve information about all VPC peering connections
peering_connections = client.describe_vpc_peering_connections()

#peering_connections = client.describe_route_tables()
#
#for connection_rt in peering_connections['RouteTables']:
#    print(connection_rt)




test = {}
# print details of each peering connection
for connection in peering_connections['VpcPeeringConnections']:
    for tag in connection['Tags']:
        test[tag['Key']] = tag['Value']
    print("connection_id = ", connection['VpcPeeringConnectionId'])
    print("peer_owner_id = ", connection['AccepterVpcInfo']['OwnerId'])
    print("peer_vpc_id = ", connection['AccepterVpcInfo']['VpcId'])
    print("vpc_id = ", connection['RequesterVpcInfo']['VpcId'])
    print("tags = ", test)
    peering_connections = client.describe_route_tables(filters=[{'Name': 'route.vpc-peering-connection-id', 'Values': [connection['VpcPeeringConnectionId']]}])['RouteTables']
    for connection_rt in peering_connections['RouteTables']:
        print(connection_rt)
 




