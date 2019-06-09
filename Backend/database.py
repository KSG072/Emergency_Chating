import sqlite3
import os
from datetime import datetime

chatfile = '../Data/chat_log.db'
userfile = '../Data/user.db'

def create_db():
    conn = sqlite3.connect(chatfile)
    cur = conn.cursor()
    table_create_sql = """CREATE TABLE IF NOT EXISTS chat_log(
    nickname VARCHAR(32) not null,
    message text not null,
    ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"""
    cur.execute(table_create_sql)

def add_chat(userid, message):
    conn = sqlite3.connect(chatfile)
    cur = conn.cursor()
    chat = "INSERT INTO chat_log(nickname, message, ts) values (?, ?, CURRENT_TIMESTAMP)"
    cur.execute(chat, (userid, message))
    conn.commit()

def list_chat(ts = None):
    log = []
    conn = sqlite3.connect(chatfile)
    cur = conn.cursor()
    if ts != None:
        sql = "select * from chat_log where chat_log.ts >= ?"
        cur.execute(sql, (ts,))
    else:
        sql = "select * from chat_log where 1"
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            log.append(row)
    return log

def create_user_db():
    conn = sqlite3.connect(userfile)
    cur = conn.cursor()
    table_create_sql = """CREATE TABLE IF NOT EXISTS user(
    id VARCHAR(32) not null,
    nick VARCHAR(32) not null default '익명',
    password text not null);"""
    cur.execute(table_create_sql)
    conn.commit()

def searchid(id):
    conn = sqlite3.connect(userfile)
    cur = conn.cursor()
    sql = "SELECT * from user where id == ?"
    cur.execute(sql, (id,))
    rows = cur.fetchall()
    return len(rows)>0

def searchpw(id, pw):
    conn = sqlite3.connect(userfile)
    cur = conn.cursor()
    sql = "SELECT password from user where id == ?"
    cur.execute(sql, (id,))
    info = cur.fetchall()
    return pw == info[0][0]

def searchnick(nick):
    if nick == "": return False
    conn = sqlite3.connect(userfile)
    cur = conn.cursor()
    sql = "SELECT nick from user where 1"
    cur.execute(sql)
    info = cur.fetchall()
    return (nick,) in info

def nick(id):
    conn = sqlite3.connect(userfile)
    cur = conn.cursor()
    sql = "SELECT nick from user where id == ?"
    cur.execute(sql, (id,))
    info = cur.fetchall()
    return info[0][0]

def list_chat_log():
    log = []
    conn = sqlite3.connect(chatfile)
    cur = conn.cursor()
    sql = "select * from chat_log where 1"
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        log.append(row)
    return log

def resister(id, nick, pw):
    conn = sqlite3.connect(userfile)
    cur = conn.cursor()
    sql = "INSERT INTO user(id, nick ,password) values (?, ?, ?)"
    cur.execute(sql, (id, nick, pw))
    conn.commit()