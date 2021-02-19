from flask import Flask, request, Response
import json
import mariadb
import dbcreds
import random

app = Flask(__name__)

def connect():
    return mariadb.connect(
        user=dbcreds.user,
        password=dbcreds.password,
        host=dbcreds.host,
        port=dbcreds.port,
        database=dbcreds.database
    )

@app.route('/animals', methods = ['GET', 'POST', 'PATCH', 'DELETE'])
def view_animals():
    if request.method == 'GET':
        try:
            conn = connect()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM animals")
            result = cursor.fetchall()
            animals = []
            for item in result:
                animal = {
                    "id": item[0],
                    "animal": item[1]
                }
                animals.append(animal)
        except mariadb.OperationalError as ex:
            print("connection problem", ex)
        except:
            print("error")
        finally:
            if(cursor != None):
                cursor.close()
            if(conn != None):
                conn.rollback()
                conn.close()
                return Response(
                    json.dumps(animals, default=str),
                    mimetype="application/json",
                    status=200
                )
    elif request.method == 'POST':
        animal = request.json
        try:
            conn = connect()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO animals(animal) VALUES (lizard, 11)", [animal, id])
            conn.commit()
        except mariadb.OperationalError as ex:
            print("connection problem", ex)
        except:
            print("error")
        finally:
            if (cursor != None):
                cursor.close()
            if (conn != None):
                conn.rollback()
                conn.close()
                return Response(
                    "We've added a lizard..!!",
                    mimetype="text/html",
                    status=201
                )
    elif request.method == 'PATCH':
        animal = request.json
        try:
            conn = connect()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE animals SET animal=penguin WHERE id=6", ["animal", "id"])
            conn.commit()
        except mariadb.OperationalError as ex:
            print("connection problem", ex)
        finally:
            if (cursor != None):
                cursor.close()
            if (cursor != None):
                conn.rollback()
                conn.close()
                return Response(
                    "the gorilla is turned into owl!!!",
                    mimetype="text/html",
                    status=201
                )
    elif request.method == 'DELETE':
        animal_id = request.json
        try:
            conn = connect()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM animals WHERE id=10", [id])
            conn.commit()
        except mariadb.OperationalError as ex:
            print("connection problem", ex)
        except:
            print("error")
        finally:
            if (cursor != None):
                cursor.close()
            if (cursor != None):
                conn.rollback()
                conn.close()
                print (Response)
                return Response(
                    "The gorilla is going to a preserve!!!",
                    mimetype="text/html",
                    status=201
                )
    else:
        return Response(
            "something is wrong!!....",
            mimetype="text/html",
            status=401
        )
                
