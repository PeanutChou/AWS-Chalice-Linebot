from chalicelib.components import do_transaction_pg

def create_relevant_tables() -> dict:
    sql = f"""
        CREATE SCHEMA IF NOT EXISTS linebot;
        CREATE SCHEMA IF NOT EXISTS linebot_internal;
        

        CREATE TABLE IF NOT EXISTS linebot.linebot_joined_group
            (
                datetime            timestamp without time zone NOT NULL,
                update_time         timestamp without time zone,
                group_id            character varying NOT NULL PRIMARY KEY,
                group_name          character varying,
                group_picture_url   character varying,
                is_left             boolean,
                is_record           boolean,
                is_transfer         boolean
            );

        CREATE TABLE IF NOT EXISTS linebot.linebot_follower_info
            (
                datetime            timestamp without time zone NOT NULL,
                update_time         timestamp without time zone,
                user_id             character varying NOT NULL PRIMARY KEY,
                user_name           character varying,
                user_picture_url    character varying,
                is_unfollow         boolean,
                is_heo_officer      boolean,
                is_subscribed       boolean
            );

        CREATE TABLE IF NOT EXISTS linebot.linebot_location_query
            (
                user_id             character varying NOT NULL PRIMARY KEY,
                datetime            timestamp without time zone,
                loc_query_type      character varying
            );
            
        CREATE TABLE IF NOT EXISTS linebot.linebot_subscribed_info
            (
                user_id             character varying NOT NULL PRIMARY KEY,
                datetime            timestamp without time zone,
                subscribed_target   character varying[]
            );

        CREATE TABLE IF NOT EXISTS linebot.linebot_notify_log
            (
                user_id_list        character varying[],
                datetime            timestamp without time zone,
                related_stn         character varying,
                scenario            character varying,
                obs_time            timestamp without time zone,
                obs_value           double precision,
                notify_target       character varying
            );

        CREATE TABLE IF NOT EXISTS linebot.linebot_flex_json
            (
                module              character varying,
                function            character varying,
                flex                json
            );

        CREATE TABLE IF NOT EXISTS linebot.linebot_usage_statistic
            (
                module              character varying,
                function            character varying,
                count               integer
            );

        CREATE TABLE IF NOT EXISTS linebot.linebot_richmenu_log
            (
                datetime            timestamp without time zone NOT NULL,
                title               character varying,
                url                 character varying,
                username            character varying
            );

        CREATE TABLE IF NOT EXISTS linebot.linebot_richmenu_id
            (
                richmenu_name       character varying,
                richmenu_id         character varying,
                richmenu_sample_json character varying
            );

        CREATE TABLE IF NOT EXISTS linebot.linebot_announcement_log
            (
                announcement_id     serial NOT NULL PRIMARY KEY,
                create_time         timestamp without time zone NOT NULL,
                user_id             character varying,
                title               character varying,
                url                 character varying,
                content             character varying,
                sent_time           timestamp without time zone,
                canceled            boolean
            );

        CREATE TABLE IF NOT EXISTS linebot.linebot_report_disaster
            (
                case_no             character varying,
                datetime            timestamp without time zone NOT NULL,
                user_id             character varying,
                user_name           character varying,
                user_picture_url    character varying,
                lon                 double precision,
                lat                 double precision,
                geom                geometry,
                msg_id              character varying NOT NULL PRIMARY KEY,
                content             character varying[],
                img_set_id          character varying,
                is_confirmed        boolean,
                is_approved         boolean
            );
    """
    do_transaction_pg.do_transaction_command_manage(config_db=setting.config_db, sql_string=sql)
    return {
        "status": True,
        "detail": "created relevant tables already"
    }