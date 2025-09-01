from Robot.Design.face import wajah # mengimpor fungsi wajah dari file face.py yang berada di dalam folder Design pada package Robot
from Robot.Design.outfit import baju # mengimpor fungsi baju dari file outfit.py yang berada di dalam folder Design pada package Robot
from Robot.Actions.walk import jalan # mengimpor fungsi jalan dari file walk.py yang berada di dalam folder Actions pada package Robot
from Robot.Actions.hello import sapa # mengimpor fungsi sapa dari file hello.py yang berada di dalam folder Actions pada package Robot
from Robot.Sound.alarm import alarm # mengimpor fungsi alarm dari file alarm.py yang berada di dalam folder Sound pada package Robot

print(wajah()) # mencetak hasil dari fungsi wajah
print(baju()) # mencetak hasil dari fungsi baju
print(jalan()) # mencetak hasil dari fungsi jalan
print(sapa()) # mencetak hasil dari fungsi sapa
print(alarm()) # mencetak hasil dari fungsi alarm