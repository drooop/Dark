import tornado.ioloop
import tornado.web
import json
import copy
import uuid

# ----------------------------------------------------------------
# 配置参数
# ----------------------------------------------------------------
PORT = 8031
# ----------------------------------------------------------------
resModel = {
    'meta': {
        'status': 401,
        'message': 'model error'
    },
    'data': {}
}

token = str(uuid.uuid4())

userid = 666

userList = [
    {
        'id': 500,
        'role_name': "超级管理员",
        'username': 'admin',
        'company': '1486720211',
        'mobile': '13950068590',
        'position': 'position_data',
        'email': 'linken@qq.com',
        'mg_state': True
    },
    {
        'id': 400,
        'role_name': "测试角色0",
        'username': 'linken0',
        'company': '1486720211',
        'mobile': '13950068591',
        'position': 'position_data',
        'email': 'linken0@qq.com',
        'mg_state': False
    },
    {
        'id': 401,
        'role_name': "测试角色1",
        'username': 'linken1',
        'company': '1486720211',
        'mobile': '13950068591',
        'position': 'position_data',
        'email': 'linken1@qq.com',
        'mg_state': False
    },
    {
        'id': 402,
        'role_name': "测试角色2",
        'username': 'linken2',
        'company': '1486720211',
        'mobile': '13950068591',
        'position': 'position_data',
        'email': 'linken2@qq.com',
        'mg_state': False
    },
    {
        'id': 403,
        'role_name': "测试角色3",
        'username': 'linken3',
        'company': '1486720211',
        'mobile': '13950068591',
        'position': 'position_data',
        'email': 'linken3@qq.com',
        'mg_state': False
    },
    {
        'id': 404,
        'role_name': "测试角色4",
        'username': 'linken4',
        'company': '1486720211',
        'mobile': '13950068591',
        'position': 'position_data',
        'email': 'linken4@qq.com',
        'mg_state': False
    },
    {
        'id': 405,
        'role_name': "测试角色5",
        'username': 'linken5',
        'company': '1486720211',
        'mobile': '13950068591', 'position': 'position_data',
        'email': 'linken5@qq.com',
        'mg_state': False
    },
    {
        'id': 406,
        'role_name': "测试角色6",
        'username': 'linken6',
        'company': '1486720211',
        'mobile': '13950068591',
        'position': 'position_data',
        'email': 'linken6@qq.com',
        'mg_state': False
    },
    {
        'id': 407,
        'role_name': "测试角色7",
        'username': 'linken7',
        'company': '1486720211',
        'mobile': '13950068591',
        'position': 'position_data',
        'email': 'linken7@qq.com',
        'mg_state': False
    },
    {
        'id': 408,
        'role_name': "测试角色8",
        'username': 'linken8',
        'company': '1486720211',
        'mobile': '13950068591',
        'position': 'position_data',
        'email': 'linken8@qq.com',
        'mg_state': False
    }
]


def menu(id, authName, path):
    return {
        'id': id,
        'authName': authName,
        'path': path
    }

# ----------------------------------------------------------------
# Handlers
# ----------------------------------------------------------------


class Hello(tornado.web.RequestHandler):
    def get(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        print('hello')
        self.write('hello')


class Login(tornado.web.RequestHandler):

    def post(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")

        try:
            data = json.loads(str(self.request.body, encoding='utf8'))
        except Exception as e:
            raise e
        else:
            res = copy.deepcopy(resModel)
            print(data)
            if data.get('password'):
                if data.get('password') == 'TQcps123':
                    res['meta']['status'] = 200
                    res['meta']['message'] = 'Login Success'
                    res['data'] = {'token': token}
                else:
                    res['meta']['status'] = 400
                    res['meta']['message'] = 'Login Failed! Password is not correct'
            else:
                res['meta']['status'] = 400
                res['meta']['message'] = 'Critical! Invalid data'
        self.write(json.dumps(res))


class Menu(tornado.web.RequestHandler):
    def get(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        res = copy.deepcopy(resModel)
        res['meta']['status'] = 200
        res['meta']['message'] = 'menu-list loading successfully'
        # Menu1
        menu1 = menu(1, '用户管理', 'user_management')
        menu1['children'] = [menu(11, '用户操作', '/user_manager'), menu(
            12, '其他', '/default')]
        # Menu2
        menu2 = menu(2, '内容管理', 'content_management')
        menu2['children'] = [menu(21, '内容操作', '/content_manager'), menu(
            22, '其他', '/default')]
        res['data'] = [menu1, menu2]
        self.write(json.dumps(res))


class User(tornado.web.RequestHandler):
    def get(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods',
                        'POST, GET, PUT, OPTIONS')
        res = copy.deepcopy(resModel)
        query = self.get_query_arguments('query', strip=True)[0]
        pageNum = int(self.get_query_arguments('pageNum', strip=True)[0])
        pageSize = int(self.get_query_arguments('pageSize', strip=True)[0])
        print('user query data:', query, pageNum, pageSize)
        if query:
            res['meta']['status'] = 200
            res['meta']['message'] = 'user-list loading successfully'
            res_data = []
            for user in userList:
                for _, v in user.items():
                    if query in str(v):
                        res_data.append(user)
            res['data'] = {
                'users': res_data,
                'total': len(userList)
            }
            self.write(json.dumps(res))
        else:
            res['meta']['status'] = 200
            res['meta']['message'] = 'user-list loading successfully'
            start_item_index = pageSize * (pageNum-1)
            end_item_index = start_item_index + pageSize
            userListReturn = userList[start_item_index:end_item_index]
            print(userListReturn)
            res['data'] = {
                'users': userListReturn,
                'total': len(userList)
            }
            self.write(json.dumps(res))

    def post(self):
        global userid
        global userList
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods',
                        'POST, GET, PUT, OPTIONS')
        res = copy.deepcopy(resModel)
        newUserInfo = str(self.request.body, encoding='utf8')
        try:
            newUserInfo = json.loads(newUserInfo)
        except Exception as e:
            # self.write(json.dumps(res))
            raise e
        else:
            print(newUserInfo)
            userid += 1
            newUserInfo['id'] = userid
            userList.append(newUserInfo)
            res['meta']['status'] = 201
            res['meta']['message'] = 'add user successfully'
            # self.write(json.dumps(res))
        finally:
            self.write(json.dumps(res))

    def put(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods',
                        'POST, GET, PUT, OPTIONS')
        self.write('ok')


class UserQuery(tornado.web.RequestHandler):
    def get(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods',
                        'POST, GET, PUT, OPTIONS')
        # print(self.get_query_arguments('id', strip=True))
        res = copy.deepcopy(resModel)
        userID = int(self.get_query_arguments('id', strip=True)[0])
        action = self.get_query_arguments('action', strip=True)[0]
        print('userID',userID, 'action', action)
        if action:
            if userID:
                for user_index in range(len(userList)):
                    if userID == userList[user_index]['id']:
                        userList.pop(user_index)
                        res['meta']['status'] = 200
                        res['meta']['message'] = 'User deleted successfully'
                        break
                else:
                    res['meta']['status'] = 400
                    res['meta']['message'] = 'Failed, please try again later...'
                self.write(json.dumps(res))
                return
        if userID:
            for user in userList:
                if userID == user['id']:
                    user_ = copy.deepcopy(user)
                    res['meta']['status'] = 200
                    res['meta']['message'] = 'UserInfo loading successfully'
                    res['data'] = user_
                    break
            else:
                res['meta']['status'] = 400
                res['meta']['message'] = 'Failed, please try again later...'
            self.write(json.dumps(res))

    def post(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods',
                        'POST, GET, PUT, OPTIONS')
        res = copy.deepcopy(resModel)
        body_data = str(self.request.body, encoding='utf8')
        try:
            data = json.loads(body_data)
            print(data)
        except Exception as e:
            res['meta']['message'] = 'can not parse new data with userID'
        else:
            userID = data.get('id')
            if userID:
                for user in userList:
                    if userID == user['id']:
                        user.update(data)
                        res['meta']['status'] = 200
                        res['meta']['message'] = 'UserInfo modifying successfully'
                        break
                else:
                    res['meta']['message'] = 'can not find corespond userID...'
        finally:
            self.write(json.dumps(res))
                   
    def delete(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods',
                        'POST, GET, PUT, DELETE, OPTIONS')
        print(self.get_query_arguments('id', strip=True))
        res = copy.deepcopy(resModel)
        userID = int(self.get_query_arguments('id', strip=True)[0])
        if userID:
            for user_index in len(userList):
                if userID == userList[user_index].id:
                    userList.pop(user_index)
                    res['meta']['status'] = 200
                    res['meta']['message'] = 'User deleted successfully'
                    break
            else:
                res['meta']['status'] = 400
                res['meta']['message'] = 'Failed, please try again later...'
            self.write(json.dumps(res))
    
    # def options(self):
    #     self.set_header("Access-Control-Allow-Origin", "*")
    #     self.set_header("Access-Control-Allow-Headers", "x-requested-with")
    #     self.set_header('Access-Control-Allow-Methods',
    #                     'POST, GET, PUT, DELETE, OPTIONS')
    #     self.write('ok')
        



def make_app():
    return tornado.web.Application([
        (r"/api/drop", Hello),
        (r"/api/login", Login),
        (r"/api/menus", Menu),
        (r"/api/users", User),
        (r"/api/users/", UserQuery)
    ], debug=True)


if __name__ == "__main__":
    app = make_app()
    app.listen(PORT, address="0.0.0.0")
    print(f'server start at {PORT}......')
    tornado.ioloop.IOLoop.current().start()
