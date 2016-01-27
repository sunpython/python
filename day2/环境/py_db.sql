/*
Navicat MySQL Data Transfer

Source Server         : wx
Source Server Version : 50520
Source Host           : wx.eyh.cn:3306
Source Database       : py_db

Target Server Type    : MYSQL
Target Server Version : 50520
File Encoding         : 65001

Date: 2016-01-27 17:04:01
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `py_cart`
-- ----------------------------
DROP TABLE IF EXISTS `py_cart`;
CREATE TABLE `py_cart` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` char(50) NOT NULL,
  `price` decimal(8,2) NOT NULL DEFAULT '0.00',
  `sl` int(11) NOT NULL DEFAULT '1',
  `uid` char(20) NOT NULL DEFAULT '0',
  `pid` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of py_cart
-- ----------------------------
INSERT INTO `py_cart` VALUES ('11', '键盘', '20.00', '1', '123', '7');

-- ----------------------------
-- Table structure for `py_product`
-- ----------------------------
DROP TABLE IF EXISTS `py_product`;
CREATE TABLE `py_product` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` char(20) DEFAULT NULL,
  `price` double(8,2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of py_product
-- ----------------------------
INSERT INTO `py_product` VALUES ('1', '苹果手机', '4888.00');
INSERT INTO `py_product` VALUES ('2', '小米手机', '2000.00');
INSERT INTO `py_product` VALUES ('3', 'python', '5300.00');
INSERT INTO `py_product` VALUES ('4', 'linux', '3200.00');
INSERT INTO `py_product` VALUES ('5', '肉包', '10.00');
INSERT INTO `py_product` VALUES ('6', '奶粉', '398.00');
INSERT INTO `py_product` VALUES ('7', '键盘', '20.00');
INSERT INTO `py_product` VALUES ('8', '径山茶', '538.00');

-- ----------------------------
-- Table structure for `py_user`
-- ----------------------------
DROP TABLE IF EXISTS `py_user`;
CREATE TABLE `py_user` (
  `id` tinyint(3) unsigned NOT NULL AUTO_INCREMENT,
  `username` char(10) NOT NULL,
  `passwd` char(32) NOT NULL,
  `regdate` int(11) NOT NULL DEFAULT '0',
  `groupid` tinyint(4) NOT NULL,
  `my_money` decimal(8,2) NOT NULL DEFAULT '20.00',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of py_user
-- ----------------------------
INSERT INTO `py_user` VALUES ('1', 'sungwd', '123', '111', '1', '7172.00');
INSERT INTO `py_user` VALUES ('33', 'moongwd', '123', '0', '1', '1000.00');
INSERT INTO `py_user` VALUES ('34', 'test', '321', '0', '1', '10000.00');
