from pyrebase import pyrebase
from Model import predict_target

# Generate random data for 6 lists                                                         
def generate_data():
    firebaseConfig = {
    'apiKey': "AIzaSyCRHiEtOod7HWAUSLb--FwtkvsxBf12p3Y",                                                                                                              
    'authDomain': "sem7-f53f5.firebaseapp.com",
    'databaseURL': "https://sem7-f53f5-default-rtdb.asia-southeast1.firebasedatabase.app",
    'projectId': "sem7-f53f5",
    'storageBucket': "sem7-f53f5.appspot.com",
    'messagingSenderId': "685201757909",
    'appId': "1:685201757909:web:b90c12e65f14b131adb45c",
    'measurementId': "G-PPMXC08EV4"
    };

    firebase = pyrebase.initialize_app(firebaseConfig)

    database = firebase.database()

    graph1 = database.child("data1").get().val()
    graph2 = database.child("data2").get().val()
    graph3 = database.child("data3").get().val()
    graph4 = database.child("data4").get().val()
    graph5 = database.child("data5").get().val()
    graph6 = database.child("data6").get().val()
    
    graph1 = graph1.values()
    graph1 = list(graph1)
    graph2 = graph2.values()
    graph2 = list(graph2)
    graph3 = graph3.values()
    graph3 = list(graph3)
    graph4 = graph4.values()
    graph4 = list(graph4)
    graph5 = graph5.values()
    graph5 = list(graph5)

    target_list = []
    target_list.append(sum(graph1))
    target_list.append(sum(graph2))
    target_list.append(sum(graph3))
    target_list.append(sum(graph4))
    target_list.append(sum(graph5))
    target_list.append(sum(graph6))
    target = predict_target(target_list)
    return graph1, graph2, graph3, graph4, graph5, graph6, target