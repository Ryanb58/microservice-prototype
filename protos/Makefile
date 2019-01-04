# build:
# 	@docker run -v `pwd`:/defs namely/protoc-all -i ./ -d ./ -l python
# 	cp -r gen/pb_python/accounts ../services/accounts/proto
# 	cp -r gen/pb_python/auth ../services/auth/proto

createvirtualenv:
	virtualenv -p python3 venv
	. venv/bin/activate
	pip install grpcio-tools


# buildit:
# 	python -m grpc_tools.protoc -I ./ --python_out=./gen/pb_python --grpc_python_out=./gen/pb_python accounts/accounts.proto auth/auth.proto
# 	cp -r gen/pb_python/accounts ../services/accounts/proto
# 	cp -r gen/pb_python/auth ../services/auth/proto


buildit-accounts:
	# python -m grpc_tools.protoc -I ./ --python_out=./gen/pb_python --grpc_python_out=./gen/pb_python accounts/accounts.proto
	# cp -r gen/pb_python/accounts ../services/accounts/proto
	python -m grpc_tools.protoc -I. --python_out=./../services/accounts/protos --grpc_python_out=./../services/accounts/protos ./accounts/accounts.proto
	python -m grpc_tools.protoc -I. --python_out=./../clients/protos --grpc_python_out=./../clients/protos ./accounts/accounts.proto

	echo "Make sure you update the imports in './../services/accounts/protos' and './../clients/protos'."