from datetime import datetime
import os

def make_time(s):
    if s < 10: return "0" + str(s)
    return str(s)

def palindrome(s): return str(s) == str(s)[::-1]
def find_palindromic_times(lz=False, tf=False, specials=True, save=False):
    if specials:
        times = {"123456"}
        if not lz: times |= {"12345"}
    else: times = set()
    for i in range(1 if not tf else 0, 12 if not tf else 24):
        for j in range(60):
            for k in range(60):
                time_stamp = (make_time(i) if lz else str(i))+make_time(j)+make_time(k)
                if palindrome(time_stamp):
                    print(time_stamp)
                    times.add(time_stamp)
    if save:
        with open(os.path.join(os.path.dirname(__file__), "resources", "timestamps.txt"), "w+") as tf:
            tf.writelines("\n".join(times))
    return times

def formatted_current_time(lz=False, tf=False):
    return datetime.now().strftime(f"X%{'I' if not tf else 'H'}:%M:%S").replace("X0", "0" if lz else "").replace("X", "").replace(":", "")

if __name__ == "__main__":
    find_palindromic_times(save=True)
    print(formatted_current_time(lz=False, tf=True))