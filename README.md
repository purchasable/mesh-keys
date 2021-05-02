# Mesh-Keys
A repo that contains all the mesh keys needed for mesh backend, along with a code example of how to use them in python


Have been seeing alot of people pay for these recently, when it really should be open sourced. the keys in the Mesh-Keys.txt are in the order key, secret key, api key. You are going to want to put the "id" first, if you are using mohawk sender, then the secret key as the "key" param in the sender function, the algorithm as sha256 stays the same. and then in the headers, you should have the x-api-key. If you run the python file it should return in text the product page details. If you would like to do post requests in this then just change the method to POST. There are other external imports around for different languages, but you can have a look for them yourself. Ty

Vastid
