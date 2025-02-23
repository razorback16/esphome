from esphome.cpp_generator import MockObj

global_ns = MockObj("", "")
void = global_ns.namespace("void")
nullptr = global_ns.namespace("nullptr")
float_ = global_ns.namespace("float")
double = global_ns.namespace("double")
bool_ = global_ns.namespace("bool")
int_ = global_ns.namespace("int")
std_ns = global_ns.namespace("std")
std_string = std_ns.class_("string")
std_vector = std_ns.class_("vector")
uint8 = global_ns.namespace("uint8_t")
uint16 = global_ns.namespace("uint16_t")
uint32 = global_ns.namespace("uint32_t")
uint64 = global_ns.namespace("uint64_t")
int32 = global_ns.namespace("int32_t")
const_char_ptr = global_ns.namespace("const char *")
NAN = global_ns.namespace("NAN")
esphome_ns = global_ns  # using namespace esphome;
App = esphome_ns.App
Nameable = esphome_ns.class_("Nameable")
Component = esphome_ns.class_("Component")
ComponentPtr = Component.operator("ptr")
PollingComponent = esphome_ns.class_("PollingComponent", Component)
Application = esphome_ns.class_("Application")
optional = esphome_ns.class_("optional")
arduino_json_ns = global_ns.namespace("ArduinoJson")
JsonObject = arduino_json_ns.class_("JsonObject")
JsonObjectRef = JsonObject.operator("ref")
JsonObjectConstRef = JsonObjectRef.operator("const")
Controller = esphome_ns.class_("Controller")
GPIOPin = esphome_ns.class_("GPIOPin")
InternalGPIOPin = esphome_ns.class_("InternalGPIOPin", GPIOPin)
gpio_ns = esphome_ns.namespace("gpio")
gpio_Flags = gpio_ns.enum("Flags", is_class=True)
