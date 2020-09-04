import socket
import urllib.request

def checknet():
    try:
        urllib.request.urlopen("http://google.com")
        return True
    except :
        return False

import csv
import cv2
import numpy as np
from notify_run import Notify

from time import sleep
from flask_opencv_streamer.streamer import Streamer
import tensorflow as tf
from utils import visualization_utils as vis_util


port = 3030
require_login = False
streamer = Streamer(port, require_login)
notify = Notify()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
add=s.getsockname()[0]
fad="http://"+add+":3030"






def detect_baby(detection_graph, category_index, is_color_recognition_enabled):

        webaccess=0
        if checknet():
                webaccess=1
                print("Connected")
        else:
                webaccess=0
                print("Not Connected")

        cap=cv2.VideoCapture(0)
        counting_mode = "..."
        width_heigh_taken = True
        height = 0
        width = 0
        counterb = 0
        notifications=1
        
   
        
        i=0
        from notify_run import Notify
        notify = Notify()
        with detection_graph.as_default():
          with tf.Session(graph=detection_graph) as sess:   
            image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
            detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
            detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
            detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
            num_detections = detection_graph.get_tensor_by_name('num_detections:0')

            
            (ret, frame) = cap.read()

            while True:
              
                (ret, frame) = cap.read()          

                if not  ret:
                    print("end of the video file...")
                    break
                
                input_frame = frame
                streamer.update_frame(frame)

                
                image_np_expanded = np.expand_dims(input_frame, axis=0)

                (boxes, scores, classes, num) = sess.run(
                    [detection_boxes, detection_scores, detection_classes, num_detections],
                    feed_dict={image_tensor: image_np_expanded})

           
                font = cv2.FONT_HERSHEY_SIMPLEX

             
                counter, csv_line, counting_mode = vis_util.visualize_boxes_and_labels_on_image_array(cap.get(1),
                                                                                                      input_frame,
                                                                                                      1,
                                                                                                      is_color_recognition_enabled,
                                                                                                      np.squeeze(boxes),
                                                                                                      np.squeeze(classes).astype(np.int32),
                                                                                                      np.squeeze(scores),
                                                                                                      category_index,
                                                                                                      use_normalized_coordinates=True,
                                                                                                      line_thickness=2)

                
                ks= cv2.waitKey(1) 
                if(ks==ord('n')):
                    if(webaccess==1):
                        if(notifications==1):
                            notifications=0
                        
                        else:
                            notifications=1
                    else:
                        notifications=0
                        
                        
                elif(ks==ord('q')):
                    break

                if(ks==ord('r')):
                    checknet()
                    if checknet():
                         webaccess=1
                    else:
                         webaccess=0
                    print(webaccess)
                
                if(webaccess==1):
                    if(counting_mode !="'baby:': 1" ):
                        
                        if(notifications==1):

                            counterb+=1
                        
                            cv2.putText(input_frame, "...", (10, 35), font, 0.7, (255,255,255),2,cv2.FONT_HERSHEY_DUPLEX) 
                            if(counterb==15):
                                print('Notification Sent: Baby not found')
                                if checknet():
                                    notify.send('Baby not found', fad)
                                counterb=0

                    elif(counting_mode=="'baby:': 1") :

                        if(notifications==1):

                            counterb=0
                            
                        
                    
                else:
                    cv2.putText(input_frame, counting_mode, (10, 35), font, 0.7, (255,255,255),2,cv2.FONT_HERSHEY_DUPLEX)
                
                if(webaccess==1):
                    if(notifications==1):
                        cv2.putText(input_frame, "Notifications:On", (10,60), font, 0.6, (255,255,255),2,cv2.FONT_HERSHEY_DUPLEX)
                    else:
                        cv2.putText(input_frame, "Notifications:Off", (10,60), font, 0.6, (255,255,255),2,cv2.FONT_HERSHEY_DUPLEX)
            
                else:
                       cv2.putText(input_frame, "Notifications:Off(No Internet Connection)", (10,60), font, 0.6, (255,255,255),2,cv2.FONT_HERSHEY_DUPLEX)
                cv2.imshow('Baby Monitoring',input_frame)
               
                if not streamer.is_streaming:
                    streamer.start_streaming()
               
        
            cap.release()
            cv2.destroyAllWindows()

