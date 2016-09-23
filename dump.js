use processing_layer
var c = db.base_data.find().limit(1000)
use material;
while(c.hasNext()){ phone = c.next().phone_number;phone_number=db.phone_number.findOne({"_id":phone});number=phone_number.phone_number;print(number) };