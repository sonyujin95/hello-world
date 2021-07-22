import pymysql
import json
import collections


def empall():
    conn = pymysql.connect(host='???',
                            user='admin',
                            password='playdata',
                            db='playdata',
                            charset='utf8')
    cur = conn.cursor()

    cur.execute("select * from emp")

    for row in cur:
        print(row)
    
    cur.close()
    conn.close()


def empall2():
    all = []
    try:
        conn = pymysql.connect(host='?????????',
                        user='admin',
                        password='playdata',
                        db='playdata',
                        charset='utf8')
        cursor = conn.cursor()
        try:
            cursor.execute("select * from emp")
            rows = cursor.fetchall()

            objects_list = []
            for row in rows:
                d = collections.OrderedDict()
                d['empno'] = row[0]
                d['ename'] = row[1]
                d['sal'] = row[2]
                objects_list.append(d)
                print(objects_list)
            all = json.dumps(objects_list)

        except Exception as e:
            print(e)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

    return all
  

if __name__ == "__main__":
    empall()

