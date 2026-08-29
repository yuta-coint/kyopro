
def main(argv):
    # このコードはコマンドライン引数と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    S, N, K = map(int,input().split())
    houses = [tuple(map(int,input().split())) for i in range(N)]
    if K == 1:
        column = [0 for i in range(S)]
        row = [0 for i in range(S)]
        for x, y, A in houses:
            column[x] += A
            row[y] += A
        ans = min(column) + min(row) 
        for x,y,A in houses:
            score = column[x] + row[y] - A
            if score < ans:
                ans = score
        print(ans)
    else:
        column = [0 for i in range(S)]
        row = [0 for i in range(S)]
        house_search = {}
        C = 10**12
        for x, y, A in houses:
            column[x] += A
            row[y] += A
            house_search[x * C + y] = A

        column_cumulative = [0]
        row_cumulative = [0]
        for i in range(S):
            column_cumulative.append(column_cumulative[-1] + column[i])
            row_cumulative.append(row_cumulative[-1] + row[i])
        
        column_width = [column_cumulative[i + K] - column_cumulative[i] for i in range(S - K + 1)]
        row_width = [row_cumulative[i + K] - row_cumulative[i] for i in range(S - K + 1)]
        
        ans = min(column_width) + min(row_width)
        
        for x, y, A in houses:
            #x,yの周りの2K-1×2K-1マスを計算する。
            nbd = [[0 for i in range(2*K-1)] for j in range(2*K-1)]
            for i in range(2 * K - 1):
                for j in range(2 * K - 1):
                    coord = (x - (K-1) + i) * C + (y-(K-1)+j)
                    if  coord in house_search:
                        nbd[i][j] = house_search[coord]
            #累積和を計算する
            nbd_cum = [[0] for i in range(2*K)]
            nbd_cum[0] = [0 for i in range(2*K)]
            for i in range(1,2*K):
                for j in range(1,2*K):
                    nbd_cum[i].append(nbd_cum[i-1][j]+nbd_cum[i][j-1]-nbd_cum[i-1][j-1]+nbd[i-1][j-1])
            
            #K×Kマスの和を計算する。
            nbd_width = [[] for i in range(K)]
            for i in range(K):
                for j in range(K):
                    nbd_width[i].append(nbd_cum[i+K][j+K]-nbd_cum[i][j+K]-nbd_cum[i+K][j]+nbd_cum[i][j])
            
            #最小値を更新しうる部分について調べ尽くす。
            for i in range(K):
                for j in range(K):
                    if 0 <= x - i < S - K + 1 and 0 <= y - j < S - K + 1:
                        score = column_width[x - i] + row_width[y - j] - nbd_width[K - 1 - i][K - 1 - j]
                        if score < ans:
                            ans = score
        print(ans)
                    
import sys
import datetime
def change_to_datetime(S):
    year = int(S[:4])
    month = int(S[5:7])
    day = int(S[8:10])
    hour = int(S[11:13])
    minute = int(S[14:16])
    second = int(S[17:19])
    return datetime.datetime(year,month,day,hour,minute,second)

def datetime_to_string(dt):
    #S = str(dt.date) + "T" + str(dt.time)
    #S = str(dt.year) + "-" + str(dt.month) + "-" + str(dt.day) + "T" + str(dt.hour) + ":" + str(dt.minute) + ":" + str(dt.second)
    return dt.strftime('%Y-%m-%dT%H:%M:%S')


def main(lines):
    N = int(lines[0])
    room_information = [(-1, -1) for i in range(1000)]
    room_set = set()
    for i in range(1,N+1):
        room_number, capacity, weekday_fee = tuple(map(int,lines[i].split()))
        room_information[room_number] = (int(capacity), int(weekday_fee))
        room_set.add(room_number)
    visitors = {}
    visitors_charge = [0 for i in range(1000)]
    room_is_occupied = [False for i in range(1000)]
    room_cleaned = [datetime.datetime(1, 1, 1) for i in range(1000)]
    sales_time_log = [0]
    sales_money_log = [0]
    start_time = datetime.datetime(1999,12,31,23,59,59)
    for i in range(N+1,len(lines)):
        request = list(lines[i].split())
        request_time = request[0]
        request_time_for_calc = change_to_datetime(request_time)
        if request[1] == "check-in":
            room_number, number_of_adults, number_of_children, days_of_stay, guest_id = int(request[2]), int(request[3]), int(request[4]), int(request[5]), request[6]
            if room_is_occupied[room_number]:
                print(request_time, 'check-in error:', room_number, 'is occupied.')
                continue
            if request_time_for_calc < room_cleaned[room_number]:
                print(request_time, 'check-in error:', room_number, 'is being cleaned.')
                continue
            if number_of_adults + number_of_children > room_information[room_number][0]:
                print(request_time, 'check-in error:', room_number, 'cannot accommodate', guest_id+'.')
                continue
            room_is_occupied[int(room_number)] = True
            start = request_time_for_calc.weekday()
            total_charge = 0
            for i in range(1, days_of_stay+1):
                if (i + start)%7 <5:
                    adults_fee = room_information[room_number][1]
                else:
                    adults_fee = (room_information[room_number][1] * 3 -1)//2 +1
                children_fee = (adults_fee * 4 - 1)//5 + 1
                total_charge += number_of_adults * adults_fee + number_of_children * children_fee
            visitors_charge[room_number] = total_charge
            visitors[guest_id] = room_number
            print(request_time, 'check-in', guest_id, 'successfully checked in to', str(room_number) + '.')
        elif request[1] == "check-out":
            guest_id, room_number, cleaning_time = request[2], int(request[3]), int(request[4])
            if not (guest_id in visitors):
                print(request_time,"check-out error:", guest_id, "does not exist.")
                continue
            if visitors[guest_id] ==-1:
                print(request_time,"check-out error:", guest_id, "does not exist.")
                continue
            if visitors[guest_id] != room_number:
                print(request_time, "check-out error:", guest_id, "is not in", str(room_number)+".")
                continue
            total_charge = visitors_charge[room_number]
            print(request_time, 'check-out', guest_id, 'has to pay', total_charge, 'to leave', str(room_number)+'.')
            visitors[guest_id] = -1
            room_is_occupied[room_number] = False
            room_cleaned[room_number] = request_time_for_calc + datetime.timedelta(minutes=cleaning_time)
            complete_time = datetime_to_string(room_cleaned[room_number])
            print('cleaning of', room_number, 'will be completed at', complete_time + '.')
            
            request_time_int = request_time_for_calc - start_time
            sales_money_log.append(sales_money_log[-1] + total_charge)
            sales_time_log.append(request_time_int.seconds)
        elif request[1] == "status":
            number_of_vacant, number_of_cleaning, number_of_occupied = 0, 0, 0
            for room_number in room_set:
                if room_is_occupied[room_number]:
                    number_of_occupied += 1
                elif request_time_for_calc < room_cleaned[room_number]:
                    number_of_cleaning += 1
                else:
                    number_of_vacant += 1
            print(request_time, "vacant:", number_of_vacant, '; cleaning in progress:', number_of_cleaning, '; occupied:', str(number_of_occupied)+'')
        elif request[1] == "sales":
            l, r = 0,0
            start_time, end_time = change_to_datetime(request[2])-start_time, change_to_datetime(request[3])-start_time
            for i in range(len(sales_time_log)):
                if start_time.seconds < sales_time_log[i]:
                    l = i
                if end_time.seconds < sales_time_log[i]:
                    r = i
            sales_sum = sales_money_log[r]-sales_money_log[l]
            print(request_time, 'sales:', str(sales_sum)+'.')
        elif request[1] == "suggestion":
            number_of_adults, number_of_children, days_of_stay, budget, guest_id = int(request[2]), int(request[3]), int(request[4]), int(request[5]), request[6]
            number_of_vacant = 0
            number_of_large_room = 0
            numbe_of_cheap_room = 0
            suggested_room_number = -1
            for room_number in room_set:
                if room_is_occupied[room_number]:
                    continue
                elif request_time_for_calc < room_cleaned[room_number]:
                    continue
                number_of_vacant += 1
                if number_of_adults + number_of_children > room_information[room_number][0]:
                    continue
                number_of_large_room += 1
                total_charge = 0
                for i in range(1, days_of_stay+1):
                    if (i + start)%7 <5:
                        adults_fee = room_information[room_number][1]
                    else:
                        adults_fee = (room_information[room_number][1] * 3 -1)//2 +1
                    children_fee = (adults_fee * 4 - 1)//5 + 1
                    total_charge += number_of_adults * adults_fee + number_of_children * children_fee
                if total_charge > budget:
                    continue
                numbe_of_cheap_room += 1
                suggested_room_number = room_number
                break
            
            if number_of_vacant == 0:
                print(request_time, 'suggestion error: all rooms are occupied or being cleaned.')
            elif number_of_large_room == 0:
                print(request_time, 'suggestion error: any rooms cannot accommodate', guest_id+'.')
            elif numbe_of_cheap_room == 0:
                print(request_time, 'suggestion error: every room is more expensive than', guest_id, 'budget.')
            else:
                print(request_time, "suggestion", guest_id, 'successfully checked in to', str(suggested_room_number)+'.')
                room_is_occupied[suggested_room_number] = True
                visitors_charge[suggested_room_number] = total_charge
                visitors[guest_id] = suggested_room_number
                

    #for i, v in enumerate(lines):
    #  print("line[{0}]: {1}".format(i, v))
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)