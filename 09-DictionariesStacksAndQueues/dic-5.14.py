import queue

que = queue.Queue()


is_working = True

curr_ticket_id = 0

def new_ticket_id():
  global curr_ticket_id
  if curr_ticket_id < 99:
    curr_ticket_id += 1
  else:
    curr_ticket_id = 0
  return curr_ticket_id
def add_client():
  id = new_ticket_id()
  que.put(id)
  print('Your ticket id is', id)
def serve_client():
  if que.empty():
    print('no clients to serve')
    return
  id = que.get()
  print('Next client is', id)

while is_working:
  operation = input('choose operation(0:exit 1:give ticket or 2:serve client)')
  if operation == '1':
    add_client()
  elif operation == '2':
    serve_client()
  elif operation == '0':
    is_working = False
  else:
    print('wrong operation')

