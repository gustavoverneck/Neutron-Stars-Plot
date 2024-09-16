import os
import matplotlib.pyplot as plt
import numpy as np
import time

def log(message):
    global logfile
    current_time = time.time()
    local_time = time.localtime(current_time)
    milliseconds = int((current_time - int(current_time)) * 1000)
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time) + f".{milliseconds:03d}"
    message = current_time + " - " + message + "\n"
    logfile.write(message)
    print(message)

def setup():
    global logfile
    log_created = 0
    if not os.path.exists('log'):
        os.makedirs('log')
        log_created = 1
    
    # Log
    log_filename = time.strftime("%Y-%m-%d-%H_%M_%S")
    logfile = open(f"log/{log_filename}.txt", "w+")
    log("Neutron Stars LSV Plotting - Log")
    log("Starting application.")
    if log_created:
        log("Log folder doesn't exists. Creating 'log' folder.")
    else:
        log("Log folder already exists. Doing nothing.")

    if not os.path.exists('data'):
        log("Data folder doesn't exists. Creating 'data' folder.")
        os.makedirs('data')
    else:
        log("Data folder already exists. Doing nothing.")

    if not os.path.exists('input'):
        log("Input folder already exists. Doing nothing.")
        os.makedirs('input')
    else:
        log("Input folder already exists. Doing nothing.")
    

class LSV_Data:
    def __init__(self, models_filename="model_list.txt", B_list_filename="B_list.txt", csi_list_filename="csi_list.txt"):
        self.B_list = []
        self.csi_list = []
        self.model_list = []
        self.model_filename = models_filename
        self.B_list_filename = B_list_filename
        self.csi_list_filename = csi_list_filename
        
        self.input_folder = 'input'
        self.data_folder = 'data'

    def importLists(self):
        # Import models list
        with open(f'{self.input_folder}/{self.model_list}') as f:
            for line in f:
                self.models.append(line)

        # Import B_list
        with open(f'{self.input_folder}/{self.B_list_filename}') as f:
            for line in f:
                self.B_list.append(line)
        
        # Import csi_list
        with open(f'{self.input_folder}/{self.csi_list_filename}') as f:
            for line in f:
                self.csi_list.append(line)

    def getData(self):
        for model in self.model_list:
            if os.path.exists(model):
                for B in self.B_list:
                    if os.path.exists(B):
                        for csi in self.csi_list:
                            if os.path.exists(csi):
                                with open(f"{self.data_folder}/{model}/{B}/tov_{csi}.out") as f:
                                    for line in f.splitlines():
                                        pass
                                    # Need to create a class to the data and then import it properly
                                log(f"Data sucessfully imported for {model}/{B}/tov_{csi}.out")
                            else:
                                log(f"File {model}/{B}/{csi} doesn't exists. Skipping.")
            else:
                log(f"Model '{model}' doesn't exists. Skipping.")
                                
   

class Data:
    def __init__(self, filename):
        pass

          
def main():
    setup() # Verify/creates folders and starts the log
    #-----------------------------------------
    data = LSV_Data()

if __name__ == '__main__':
    main()