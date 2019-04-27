-- CREATE TABLE ih_house_info (
--     hi_house_id bigint unsigned NOT NULL AUTO_INCREMENT COMMENT '房屋id',
--     hi_user_id bigint unsigned NOT NULL COMMENT '用户ID',
--     hi_title varchar(64) NOT NULL COMMENT '房屋名称',
--     hi_price int unsigned NOT NULL DEFAULT '0' COMMENT '房屋价格，单位分',
--     hi_area_id bigint unsigned NOT NULL COMMENT '房屋区域ID',
--     hi_address varchar(512) NOT NULL DEFAULT '' COMMENT '地址',
--     hi_room_count tinyint unsigned NOT NULL DEFAULT '1' COMMENT '房间数',
--     hi_acreage int unsigned unsigned NOT NULL DEFAULT '0' COMMENT '房屋面积',
--     hi_house_unit varchar(32) NOT NULL DEFAULT '' COMMENT '房屋户型',
--     hi_capacity int unsigned NOT NULL DEFAULT '1' COMMENT '容纳人数',
--     hi_beds varchar(64) NOT NULL DEFAULT '' COMMENT '床的配置',
--     hi_deposit int unsigned NOT NULL DEFAULT '0' COMMENT '押金，单位分',
--     hi_min_days int unsigned NOT NULL DEFAULT '1' COMMENT '最短入住时间',
--     hi_max_days int unsigned NOT NULL DEFAULT '0' COMMENT '最长入住时间，0-不限制',
--     hi_order_count int unsigned NOT NULL DEFAULT '0' COMMENT '下单数量',
--     hi_verify_status tinyint NOT NULL DEFAULT '0' COMMENT '审核状态，0-待审核，1-审核未通过，2-审核通过',
--     hi_online_status tinyint NOT NULL DEFAULT '1' COMMENT '0-下线，1-上线',
--     hi_index_image_url varchar(256) NULL COMMENT '房屋主图片url',
--     hi_utime datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最后更新时间',
--     hi_ctime datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
--     PRIMARY KEY (hi_house_id),
--     KEY `hi_status` (hi_verify_status, hi_online_status),
--     CONSTRAINT FOREIGN KEY (`hi_user_id`) REFERENCES `ih_user_profile` (`up_user_id`),
--     CONSTRAINT FOREIGN KEY (`hi_area_id`) REFERENCES `ih_area_info` (`ai_area_id`)
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='房屋信息表';
--

use ihome;

insert into ih_house_info (hi_user_id, hi_title, hi_area_id) values(10001, "海景别墅", 1);