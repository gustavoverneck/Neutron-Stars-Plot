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

        self.data = []

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
            if os.path.exists(f"{self.data_folder}/{model}"):
                for B in self.B_list:
                    if os.path.exists(f"{self.data_folder}/{model}/{B}"):
                        for csi in self.csi_list:
                            if os.path.exists(f"{self.data_folder}/{model}/{B}/{csi}/tov_{csi}.out"):
                                with open(f"{self.data_folder}/{model}/{B}/{csi}/tov_{csi}.out") as f:
                                    model_=model; B_=B; csi_=csi;
                                    e_=[]; p_=[]; M_=[]; R_=[]
                                    for line in f.splitlines():
                                        line = line.split()
                                        e_.append(float(line[0]))
                                        p_.append(float(line[1]))
                                        M_.append(float(line[2]))
                                        R_.append(float(line[3]))
                                    data_ = subData(model=model_, B=B_, csi=csi_, e=e_, p=p_, M=M_, R=R_)
                                    self.data.append(data_)
                                log(f"Data sucessfully imported for {model}/{B}/tov_{csi}.out")
                            else:
                                log(f"Data for {model}/{B}/{csi} doesn't exists. Skipping.")
            else:
                log(f"Model '{model}' doesn't exists. Skipping.")
        log("All data imported.")
        del e_, p_, M_, R_, model_, B_, csi_
    
    def plotData(self):
        pass   # Plot data
   

class subData:
    def __init__(self, model, B, csi, e, p, M, R):
        self.model = model
        self.B = B
        self.csi = csi
        self.e = e
        self.p = p
        self.M = M
        self.R = R
    
    def __str__(self):
        return f"Model: {self.model}, B: {self.B}, csi: {self.csi}"
          
def main():
    setup() # Verify and creates folders and starts the log
    data = LSV_Data()

if __name__ == '__main__':
    main()