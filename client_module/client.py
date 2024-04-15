#!/usr/bin/env python3

import sys
from pprint import pprint

#-------------------------------
import common
from common import print_format
from class_manager import Client
from util_functions import (
    load_args, 
    load_config_file,
    subscription_start
)
    
def main():
    #Get args by user
    load_args()
    #Load config client file
    client = load_config_file()

    #subscription
    subscription_start(client)

    #print_format(str(client))

    

if __name__ == "__main__":
    main()