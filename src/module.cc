#include <nan.h>
#include <wiredtiger.h>

using namespace v8;

void init(v8::Handle<v8::Object> exports) {
    WT_CONNECTION *conn;
    //WT_CURSOR *cursor;
    WT_SESSION *session;
    //const char *key, *value;
    int ret;

    /* Open a connection to the database, creating it if necessary. */
    if ((ret = wiredtiger_open("TESTWT", NULL, "create", &conn)) != 0 ||
        (ret = conn->open_session(conn, NULL, NULL, &session)) != 0) {
        fprintf(stderr, "Error connecting to %s: %s\n",
            "TESTWT", wiredtiger_strerror(ret));
    }
}

NODE_MODULE(kv_wiredtiger, init);