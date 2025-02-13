from livereload import Server, shell

server = Server()
server.watch('index.html')
server.watch('player.js')
server.serve(root='.')
