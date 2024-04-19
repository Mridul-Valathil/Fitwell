/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.6.12-log : Database - fitwell
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`fitwell` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `fitwell`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=82 DEFAULT CHARSET=latin1;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add allocate',7,'add_allocate'),(20,'Can change allocate',7,'change_allocate'),(21,'Can delete allocate',7,'delete_allocate'),(22,'Can add batch',8,'add_batch'),(23,'Can change batch',8,'change_batch'),(24,'Can delete batch',8,'delete_batch'),(25,'Can add cart',9,'add_cart'),(26,'Can change cart',9,'change_cart'),(27,'Can delete cart',9,'delete_cart'),(28,'Can add chat',10,'add_chat'),(29,'Can change chat',10,'change_chat'),(30,'Can delete chat',10,'delete_chat'),(31,'Can add complaint',11,'add_complaint'),(32,'Can change complaint',11,'change_complaint'),(33,'Can delete complaint',11,'delete_complaint'),(34,'Can add diet',12,'add_diet'),(35,'Can change diet',12,'change_diet'),(36,'Can delete diet',12,'delete_diet'),(37,'Can add feedback',13,'add_feedback'),(38,'Can change feedback',13,'change_feedback'),(39,'Can delete feedback',13,'delete_feedback'),(40,'Can add health',14,'add_health'),(41,'Can change health',14,'change_health'),(42,'Can delete health',14,'delete_health'),(43,'Can add login',15,'add_login'),(44,'Can change login',15,'change_login'),(45,'Can delete login',15,'delete_login'),(46,'Can add order',16,'add_order'),(47,'Can change order',16,'change_order'),(48,'Can delete order',16,'delete_order'),(49,'Can add ordersub',17,'add_ordersub'),(50,'Can change ordersub',17,'change_ordersub'),(51,'Can delete ordersub',17,'delete_ordersub'),(52,'Can add payment',18,'add_payment'),(53,'Can change payment',18,'change_payment'),(54,'Can delete payment',18,'delete_payment'),(55,'Can add product',19,'add_product'),(56,'Can change product',19,'change_product'),(57,'Can delete product',19,'delete_product'),(58,'Can add questinare',20,'add_questinare'),(59,'Can change questinare',20,'change_questinare'),(60,'Can delete questinare',20,'delete_questinare'),(61,'Can add rating',21,'add_rating'),(62,'Can change rating',21,'change_rating'),(63,'Can delete rating',21,'delete_rating'),(64,'Can add request',22,'add_request'),(65,'Can change request',22,'change_request'),(66,'Can delete request',22,'delete_request'),(67,'Can add shops',23,'add_shops'),(68,'Can change shops',23,'change_shops'),(69,'Can delete shops',23,'delete_shops'),(70,'Can add tips',24,'add_tips'),(71,'Can change tips',24,'change_tips'),(72,'Can delete tips',24,'delete_tips'),(73,'Can add trainer',25,'add_trainer'),(74,'Can change trainer',25,'change_trainer'),(75,'Can delete trainer',25,'delete_trainer'),(76,'Can add user',26,'add_user'),(77,'Can change user',26,'change_user'),(78,'Can delete user',26,'delete_user'),(79,'Can add workout',27,'add_workout'),(80,'Can change workout',27,'change_workout'),(81,'Can delete workout',27,'delete_workout');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'FitWell','allocate'),(8,'FitWell','batch'),(9,'FitWell','cart'),(10,'FitWell','chat'),(11,'FitWell','complaint'),(12,'FitWell','diet'),(13,'FitWell','feedback'),(14,'FitWell','health'),(15,'FitWell','login'),(16,'FitWell','order'),(17,'FitWell','ordersub'),(18,'FitWell','payment'),(19,'FitWell','product'),(20,'FitWell','questinare'),(21,'FitWell','rating'),(22,'FitWell','request'),(23,'FitWell','shops'),(24,'FitWell','tips'),(25,'FitWell','trainer'),(26,'FitWell','user'),(27,'FitWell','workout'),(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (1,'FitWell','0001_initial','2023-12-01 07:49:08.347612'),(2,'contenttypes','0001_initial','2023-12-01 07:49:09.542081'),(3,'auth','0001_initial','2023-12-01 07:49:24.846949'),(4,'admin','0001_initial','2023-12-01 07:49:28.388179'),(5,'admin','0002_logentry_remove_auto_add','2023-12-01 07:49:28.450695'),(6,'contenttypes','0002_remove_content_type_name','2023-12-01 07:49:31.046408'),(7,'auth','0002_alter_permission_name_max_length','2023-12-01 07:49:32.304849'),(8,'auth','0003_alter_user_email_max_length','2023-12-01 07:49:33.404713'),(9,'auth','0004_alter_user_username_opts','2023-12-01 07:49:33.483854'),(10,'auth','0005_alter_user_last_login_null','2023-12-01 07:49:34.587047'),(11,'auth','0006_require_contenttypes_0002','2023-12-01 07:49:34.644960'),(12,'auth','0007_alter_validators_add_error_messages','2023-12-01 07:49:34.687225'),(13,'auth','0008_alter_user_username_max_length','2023-12-01 07:49:36.391730'),(14,'auth','0009_alter_user_last_name_max_length','2023-12-01 07:49:37.271870'),(15,'sessions','0001_initial','2023-12-01 07:49:38.247539'),(16,'FitWell','0002_auto_20231201_1558','2023-12-01 10:29:18.165548'),(17,'FitWell','0003_batch_batchname','2023-12-01 10:45:34.826786');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_session` */

/*Table structure for table `fitwell_allocate` */

DROP TABLE IF EXISTS `fitwell_allocate`;

CREATE TABLE `fitwell_allocate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Time` varchar(100) NOT NULL,
  `date` varchar(100) NOT NULL,
  `TRAINER_id` int(11) NOT NULL,
  `BATCH_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FitWell_allocate_TRAINER_id_f32ec25b_fk_FitWell_trainer_id` (`TRAINER_id`),
  KEY `FitWell_allocate_BATCH_id_1de4b961_fk_FitWell_user_id` (`BATCH_id`),
  CONSTRAINT `FitWell_allocate_BATCH_id_1de4b961_fk_FitWell_user_id` FOREIGN KEY (`BATCH_id`) REFERENCES `fitwell_user` (`id`),
  CONSTRAINT `FitWell_allocate_TRAINER_id_f32ec25b_fk_FitWell_trainer_id` FOREIGN KEY (`TRAINER_id`) REFERENCES `fitwell_trainer` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `fitwell_allocate` */

/*Table structure for table `fitwell_batch` */

DROP TABLE IF EXISTS `fitwell_batch`;

CREATE TABLE `fitwell_batch` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Fromtime` varchar(100) NOT NULL,
  `Totime` varchar(100) NOT NULL,
  `Batchname` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `fitwell_batch` */

insert  into `fitwell_batch`(`id`,`Fromtime`,`Totime`,`Batchname`) values (1,'5:00','7:00','morning');

/*Table structure for table `fitwell_cart` */

DROP TABLE IF EXISTS `fitwell_cart`;

CREATE TABLE `fitwell_cart` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `itemname` varchar(100) NOT NULL,
  `cartview` varchar(100) NOT NULL,
  `USER_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FitWell_cart_USER_id_f38507d7_fk_FitWell_user_id` (`USER_id`),
  CONSTRAINT `FitWell_cart_USER_id_f38507d7_fk_FitWell_user_id` FOREIGN KEY (`USER_id`) REFERENCES `fitwell_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `fitwell_cart` */

/*Table structure for table `fitwell_chat` */

DROP TABLE IF EXISTS `fitwell_chat`;

CREATE TABLE `fitwell_chat` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sender` varchar(100) NOT NULL,
  `receiver` varchar(100) NOT NULL,
  `date` varchar(100) NOT NULL,
  `time` varchar(100) NOT NULL,
  `TRAINER_id` int(11) NOT NULL,
  `USER_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FitWell_chat_TRAINER_id_7739c353_fk_FitWell_trainer_id` (`TRAINER_id`),
  KEY `FitWell_chat_USER_id_db6827ce_fk_FitWell_user_id` (`USER_id`),
  CONSTRAINT `FitWell_chat_USER_id_db6827ce_fk_FitWell_user_id` FOREIGN KEY (`USER_id`) REFERENCES `fitwell_user` (`id`),
  CONSTRAINT `FitWell_chat_TRAINER_id_7739c353_fk_FitWell_trainer_id` FOREIGN KEY (`TRAINER_id`) REFERENCES `fitwell_trainer` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `fitwell_chat` */

/*Table structure for table `fitwell_complaint` */

DROP TABLE IF EXISTS `fitwell_complaint`;

CREATE TABLE `fitwell_complaint` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `complaints` varchar(100) NOT NULL,
  `complaintdate` varchar(100) NOT NULL,
  `reply` varchar(100) NOT NULL,
  `replydate` varchar(100) NOT NULL,
  `TRAINER_id` int(11) NOT NULL,
  `USER_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FitWell_complaint_TRAINER_id_176aae21_fk_FitWell_trainer_id` (`TRAINER_id`),
  KEY `FitWell_complaint_USER_id_3e105a2f_fk_FitWell_user_id` (`USER_id`),
  CONSTRAINT `FitWell_complaint_USER_id_3e105a2f_fk_FitWell_user_id` FOREIGN KEY (`USER_id`) REFERENCES `fitwell_user` (`id`),
  CONSTRAINT `FitWell_complaint_TRAINER_id_176aae21_fk_FitWell_trainer_id` FOREIGN KEY (`TRAINER_id`) REFERENCES `fitwell_trainer` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `fitwell_complaint` */

/*Table structure for table `fitwell_diet` */

DROP TABLE IF EXISTS `fitwell_diet`;

CREATE TABLE `fitwell_diet` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `time` varchar(100) NOT NULL,
  `item` varchar(100) NOT NULL,
  `TRAINER_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FitWell_diet_TRAINER_id_cfb73ec3_fk_FitWell_trainer_id` (`TRAINER_id`),
  CONSTRAINT `FitWell_diet_TRAINER_id_cfb73ec3_fk_FitWell_trainer_id` FOREIGN KEY (`TRAINER_id`) REFERENCES `fitwell_trainer` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `fitwell_diet` */

/*Table structure for table `fitwell_feedback` */

DROP TABLE IF EXISTS `fitwell_feedback`;

CREATE TABLE `fitwell_feedback` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Time` varchar(100) NOT NULL,
  `date` varchar(100) NOT NULL,
  `feedback` varchar(100) NOT NULL,
  `TRAINER_id` int(11) NOT NULL,
  `USER_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FitWell_feedback_TRAINER_id_e4ad2521_fk_FitWell_trainer_id` (`TRAINER_id`),
  KEY `FitWell_feedback_USER_id_a640882e_fk_FitWell_user_id` (`USER_id`),
  CONSTRAINT `FitWell_feedback_USER_id_a640882e_fk_FitWell_user_id` FOREIGN KEY (`USER_id`) REFERENCES `fitwell_user` (`id`),
  CONSTRAINT `FitWell_feedback_TRAINER_id_e4ad2521_fk_FitWell_trainer_id` FOREIGN KEY (`TRAINER_id`) REFERENCES `fitwell_trainer` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `fitwell_feedback` */

/*Table structure for table `fitwell_health` */

DROP TABLE IF EXISTS `fitwell_health`;

CREATE TABLE `fitwell_health` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `height` varchar(100) NOT NULL,
  `weight` varchar(100) NOT NULL,
  `alergies` varchar(100) NOT NULL,
  `medicalhistory` varchar(100) NOT NULL,
  `USER_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FitWell_health_USER_id_d10aec46_fk_FitWell_user_id` (`USER_id`),
  CONSTRAINT `FitWell_health_USER_id_d10aec46_fk_FitWell_user_id` FOREIGN KEY (`USER_id`) REFERENCES `fitwell_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `fitwell_health` */

/*Table structure for table `fitwell_login` */

DROP TABLE IF EXISTS `fitwell_login`;

CREATE TABLE `fitwell_login` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `usertype` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `fitwell_login` */

insert  into `fitwell_login`(`id`,`username`,`password`,`usertype`) values (1,'Mridul','98765','admin'),(2,'muza@gmail.com','123456789','trainer');

/*Table structure for table `fitwell_order` */

DROP TABLE IF EXISTS `fitwell_order`;

CREATE TABLE `fitwell_order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status` varchar(100) NOT NULL,
  `date` varchar(100) NOT NULL,
  `paymentdate` varchar(100) NOT NULL,
  `paymentstatus` varchar(100) NOT NULL,
  `USER_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FitWell_order_USER_id_5b9e9a6c_fk_FitWell_user_id` (`USER_id`),
  CONSTRAINT `FitWell_order_USER_id_5b9e9a6c_fk_FitWell_user_id` FOREIGN KEY (`USER_id`) REFERENCES `fitwell_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `fitwell_order` */

/*Table structure for table `fitwell_ordersub` */

DROP TABLE IF EXISTS `fitwell_ordersub`;

CREATE TABLE `fitwell_ordersub` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `quantity` varchar(100) NOT NULL,
  `ORDER_id` int(11) NOT NULL,
  `PRODUCT_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FitWell_ordersub_ORDER_id_d7ebfaf3_fk_FitWell_order_id` (`ORDER_id`),
  KEY `FitWell_ordersub_PRODUCT_id_dbd0b85d_fk_FitWell_product_id` (`PRODUCT_id`),
  CONSTRAINT `FitWell_ordersub_PRODUCT_id_dbd0b85d_fk_FitWell_product_id` FOREIGN KEY (`PRODUCT_id`) REFERENCES `fitwell_product` (`id`),
  CONSTRAINT `FitWell_ordersub_ORDER_id_d7ebfaf3_fk_FitWell_order_id` FOREIGN KEY (`ORDER_id`) REFERENCES `fitwell_order` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `fitwell_ordersub` */

/*Table structure for table `fitwell_payment` */

DROP TABLE IF EXISTS `fitwell_payment`;

CREATE TABLE `fitwell_payment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `paymenttype` varchar(100) NOT NULL,
  `paymentdate` varchar(100) NOT NULL,
  `paymenttime` varchar(100) NOT NULL,
  `fee` varchar(100) NOT NULL,
  `USER_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FitWell_payment_USER_id_957f0354_fk_FitWell_user_id` (`USER_id`),
  CONSTRAINT `FitWell_payment_USER_id_957f0354_fk_FitWell_user_id` FOREIGN KEY (`USER_id`) REFERENCES `fitwell_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `fitwell_payment` */

/*Table structure for table `fitwell_product` */

DROP TABLE IF EXISTS `fitwell_product`;

CREATE TABLE `fitwell_product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `itemname` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `itemtype` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `fitwell_product` */

/*Table structure for table `fitwell_questinare` */

DROP TABLE IF EXISTS `fitwell_questinare`;

CREATE TABLE `fitwell_questinare` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `questions` varchar(100) NOT NULL,
  `answers` varchar(100) NOT NULL,
  `USER_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FitWell_questinare_USER_id_ed838883_fk_FitWell_user_id` (`USER_id`),
  CONSTRAINT `FitWell_questinare_USER_id_ed838883_fk_FitWell_user_id` FOREIGN KEY (`USER_id`) REFERENCES `fitwell_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `fitwell_questinare` */

/*Table structure for table `fitwell_rating` */

DROP TABLE IF EXISTS `fitwell_rating`;

CREATE TABLE `fitwell_rating` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rating` varchar(100) NOT NULL,
  `date` varchar(100) NOT NULL,
  `TRAINER_id` int(11) NOT NULL,
  `USER_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FitWell_rating_TRAINER_id_60206e60_fk_FitWell_trainer_id` (`TRAINER_id`),
  KEY `FitWell_rating_USER_id_89e798e2_fk_FitWell_user_id` (`USER_id`),
  CONSTRAINT `FitWell_rating_USER_id_89e798e2_fk_FitWell_user_id` FOREIGN KEY (`USER_id`) REFERENCES `fitwell_user` (`id`),
  CONSTRAINT `FitWell_rating_TRAINER_id_60206e60_fk_FitWell_trainer_id` FOREIGN KEY (`TRAINER_id`) REFERENCES `fitwell_trainer` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `fitwell_rating` */

/*Table structure for table `fitwell_request` */

DROP TABLE IF EXISTS `fitwell_request`;

CREATE TABLE `fitwell_request` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Time` varchar(100) NOT NULL,
  `date` varchar(100) NOT NULL,
  `requeststate` varchar(100) NOT NULL,
  `BATCH_id` int(11) NOT NULL,
  `USER_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FitWell_request_USER_id_9c6346ec_fk_FitWell_user_id` (`USER_id`),
  KEY `FitWell_request_BATCH_id_49e8ebcc_fk_FitWell_trainer_id` (`BATCH_id`),
  CONSTRAINT `FitWell_request_BATCH_id_49e8ebcc_fk_FitWell_trainer_id` FOREIGN KEY (`BATCH_id`) REFERENCES `fitwell_trainer` (`id`),
  CONSTRAINT `FitWell_request_USER_id_9c6346ec_fk_FitWell_user_id` FOREIGN KEY (`USER_id`) REFERENCES `fitwell_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `fitwell_request` */

/*Table structure for table `fitwell_shops` */

DROP TABLE IF EXISTS `fitwell_shops`;

CREATE TABLE `fitwell_shops` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `itemname` varchar(100) NOT NULL,
  `availability` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `fitwell_shops` */

/*Table structure for table `fitwell_tips` */

DROP TABLE IF EXISTS `fitwell_tips`;

CREATE TABLE `fitwell_tips` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tips` varchar(100) NOT NULL,
  `TRAINER_id` int(11) NOT NULL,
  `USER_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FitWell_tips_TRAINER_id_adf259f0_fk_FitWell_trainer_id` (`TRAINER_id`),
  KEY `FitWell_tips_USER_id_a282e863_fk_FitWell_user_id` (`USER_id`),
  CONSTRAINT `FitWell_tips_USER_id_a282e863_fk_FitWell_user_id` FOREIGN KEY (`USER_id`) REFERENCES `fitwell_user` (`id`),
  CONSTRAINT `FitWell_tips_TRAINER_id_adf259f0_fk_FitWell_trainer_id` FOREIGN KEY (`TRAINER_id`) REFERENCES `fitwell_trainer` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `fitwell_tips` */

/*Table structure for table `fitwell_trainer` */

DROP TABLE IF EXISTS `fitwell_trainer`;

CREATE TABLE `fitwell_trainer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `pin` varchar(100) NOT NULL,
  `latitude` varchar(100) NOT NULL,
  `longitude` varchar(100) NOT NULL,
  `LOGIN_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FitWell_trainer_LOGIN_id_75ffac64_fk_FitWell_login_id` (`LOGIN_id`),
  CONSTRAINT `FitWell_trainer_LOGIN_id_75ffac64_fk_FitWell_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `fitwell_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `fitwell_trainer` */

insert  into `fitwell_trainer`(`id`,`username`,`email`,`phone`,`place`,`post`,`pin`,`latitude`,`longitude`,`LOGIN_id`) values (1,'jeevan','jeevan@hotmail.com','9067231245553','cherkkala','karimbm','65413','','',1),(2,'jeevan','jeevan@hotmail.com','9067231245553','cherkkala','karimbm','65413','','',1),(3,'jeevan','jeevan@hotmail.com','9067231245553','cherkkala','karimbm','65413','','',1),(4,'jeevan','jeevan@hotmail.com','9067231245553','cherkkala','karimbm','65413','','',1),(5,'anjay','anjay@gmail.com','456312168492','kannapuram','mottammal','670331','','',1),(6,'muza','muza@gmail.com','4562531574','udayagiri','udayagiri','670571','','',2);

/*Table structure for table `fitwell_user` */

DROP TABLE IF EXISTS `fitwell_user`;

CREATE TABLE `fitwell_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `pin` varchar(100) NOT NULL,
  `latitude` varchar(100) NOT NULL,
  `longitude` varchar(100) NOT NULL,
  `LOGIN_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FitWell_user_LOGIN_id_559297cb_fk_FitWell_login_id` (`LOGIN_id`),
  CONSTRAINT `FitWell_user_LOGIN_id_559297cb_fk_FitWell_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `fitwell_login` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `fitwell_user` */

/*Table structure for table `fitwell_workout` */

DROP TABLE IF EXISTS `fitwell_workout`;

CREATE TABLE `fitwell_workout` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `workouttype` varchar(100) NOT NULL,
  `duration` varchar(100) NOT NULL,
  `TRAINER_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FitWell_workout_TRAINER_id_b063a373_fk_FitWell_trainer_id` (`TRAINER_id`),
  CONSTRAINT `FitWell_workout_TRAINER_id_b063a373_fk_FitWell_trainer_id` FOREIGN KEY (`TRAINER_id`) REFERENCES `fitwell_trainer` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `fitwell_workout` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
