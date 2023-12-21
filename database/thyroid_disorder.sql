-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Nov 22, 2023 at 10:19 AM
-- Server version: 10.4.10-MariaDB
-- PHP Version: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `thyroid_disorder`
--
CREATE DATABASE IF NOT EXISTS `thyroid_disorder` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `thyroid_disorder`;

-- --------------------------------------------------------

--
-- Table structure for table `ada_algo`
--

DROP TABLE IF EXISTS `ada_algo`;
CREATE TABLE IF NOT EXISTS `ada_algo` (
  `ADA_ID` int(11) NOT NULL AUTO_INCREMENT,
  `Accuracy` longtext NOT NULL,
  `Precession` longtext NOT NULL,
  `F1_Score` longtext NOT NULL,
  `Recall` longtext NOT NULL,
  `Name` longtext NOT NULL,
  PRIMARY KEY (`ADA_ID`)
) ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ada_algo`
--

INSERT INTO `ada_algo` (`ADA_ID`, `Accuracy`, `Precession`, `F1_Score`, `Recall`, `Name`) VALUES
(1, '99.57', '99.56', '99.57', '99.57', 'XG Boost Algorithm'),
(2, '99.35', '99.36', '99.35', '99.35', 'XG Boost Algorithm'),
(3, '99.71', '99.7', '99.72', '99.72', 'XG Boost Algorithm'),
(4, '99.5', '99.5', '99.49', '99.49', 'XG Boost Algorithm'),
(5, '99.57', '99.56', '99.57', '99.57', 'XG Boost Algorithm'),
(6, '99.64', '99.64', '99.64', '99.64', 'XG Boost Algorithm'),
(7, '99.71', '99.71', '99.72', '99.72', 'XG Boost Algorithm'),
(8, '99.5', '99.49', '99.5', '99.5', 'XG Boost Algorithm'),
(9, '99.71', '99.71', '99.71', '99.71', 'XG Boost Algorithm'),
(10, '99.71', '99.7', '99.72', '99.72', 'ADA Boost Algorithm'),
(11, '99.57', '99.56', '99.57', '99.57', 'ADA Boost Algorithm'),
(12, '99.43', '99.42', '99.43', '99.43', 'ADA Boost Algorithm'),
(13, '99.64', '99.63', '99.65', '99.65', 'ADA Boost Algorithm'),
(14, '99.57', '99.57', '99.57', '99.57', 'ADA Boost Algorithm'),
(15, '99.5', '99.5', '99.49', '99.49', 'ADA Boost Algorithm'),
(16, '99.43', '99.43', '99.42', '99.42', 'ADA Boost Algorithm'),
(17, '99.57', '99.56', '99.57', '99.57', 'ADA Boost Algorithm');

-- --------------------------------------------------------

--
-- Table structure for table `all_users`
--

DROP TABLE IF EXISTS `all_users`;
CREATE TABLE IF NOT EXISTS `all_users` (
  `User_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_Profile` varchar(100) NOT NULL,
  `User_Email` varchar(50) NOT NULL,
  `User_Status` varchar(10) NOT NULL,
  PRIMARY KEY (`User_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=89 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add user_details', 7, 'add_user_details'),
(26, 'Can change user_details', 7, 'change_user_details'),
(27, 'Can delete user_details', 7, 'delete_user_details'),
(28, 'Can view user_details', 7, 'view_user_details'),
(29, 'Can add dataset', 8, 'add_dataset'),
(30, 'Can change dataset', 8, 'change_dataset'),
(31, 'Can delete dataset', 8, 'delete_dataset'),
(32, 'Can view dataset', 8, 'view_dataset'),
(33, 'Can add upload_dataset_model', 9, 'add_upload_dataset_model'),
(34, 'Can change upload_dataset_model', 9, 'change_upload_dataset_model'),
(35, 'Can delete upload_dataset_model', 9, 'delete_upload_dataset_model'),
(36, 'Can view upload_dataset_model', 9, 'view_upload_dataset_model'),
(37, 'Can add dataset', 10, 'add_dataset'),
(38, 'Can change dataset', 10, 'change_dataset'),
(39, 'Can delete dataset', 10, 'delete_dataset'),
(40, 'Can view dataset', 10, 'view_dataset'),
(41, 'Can add feedback', 11, 'add_feedback'),
(42, 'Can change feedback', 11, 'change_feedback'),
(43, 'Can delete feedback', 11, 'delete_feedback'),
(44, 'Can view feedback', 11, 'view_feedback'),
(45, 'Can add ad a_algo', 12, 'add_ada_algo'),
(46, 'Can change ad a_algo', 12, 'change_ada_algo'),
(47, 'Can delete ad a_algo', 12, 'delete_ada_algo'),
(48, 'Can view ad a_algo', 12, 'view_ada_algo'),
(49, 'Can add all_users_model', 13, 'add_all_users_model'),
(50, 'Can change all_users_model', 13, 'change_all_users_model'),
(51, 'Can delete all_users_model', 13, 'delete_all_users_model'),
(52, 'Can view all_users_model', 13, 'view_all_users_model'),
(53, 'Can add d t_algo', 14, 'add_dt_algo'),
(54, 'Can change d t_algo', 14, 'change_dt_algo'),
(55, 'Can delete d t_algo', 14, 'delete_dt_algo'),
(56, 'Can view d t_algo', 14, 'view_dt_algo'),
(57, 'Can add g d_algo', 15, 'add_gd_algo'),
(58, 'Can change g d_algo', 15, 'change_gd_algo'),
(59, 'Can delete g d_algo', 15, 'delete_gd_algo'),
(60, 'Can view g d_algo', 15, 'view_gd_algo'),
(61, 'Can add kn n_algo', 16, 'add_knn_algo'),
(62, 'Can change kn n_algo', 16, 'change_knn_algo'),
(63, 'Can delete kn n_algo', 16, 'delete_knn_algo'),
(64, 'Can view kn n_algo', 16, 'view_knn_algo'),
(65, 'Can add logistic', 17, 'add_logistic'),
(66, 'Can change logistic', 17, 'change_logistic'),
(67, 'Can delete logistic', 17, 'delete_logistic'),
(68, 'Can view logistic', 17, 'view_logistic'),
(69, 'Can add random forest', 18, 'add_randomforest'),
(70, 'Can change random forest', 18, 'change_randomforest'),
(71, 'Can delete random forest', 18, 'delete_randomforest'),
(72, 'Can view random forest', 18, 'view_randomforest'),
(73, 'Can add sv m_algo', 19, 'add_svm_algo'),
(74, 'Can change sv m_algo', 19, 'change_svm_algo'),
(75, 'Can delete sv m_algo', 19, 'delete_svm_algo'),
(76, 'Can view sv m_algo', 19, 'view_svm_algo'),
(77, 'Can add x g_algo', 20, 'add_xg_algo'),
(78, 'Can change x g_algo', 20, 'change_xg_algo'),
(79, 'Can delete x g_algo', 20, 'delete_xg_algo'),
(80, 'Can view x g_algo', 20, 'view_xg_algo'),
(81, 'Can add last_login', 21, 'add_last_login'),
(82, 'Can change last_login', 21, 'change_last_login'),
(83, 'Can delete last_login', 21, 'delete_last_login'),
(84, 'Can view last_login', 21, 'view_last_login'),
(85, 'Can add predict_details', 22, 'add_predict_details'),
(86, 'Can change predict_details', 22, 'change_predict_details'),
(87, 'Can delete predict_details', 22, 'delete_predict_details'),
(88, 'Can view predict_details', 22, 'view_predict_details');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `dataset`
--

DROP TABLE IF EXISTS `dataset`;
CREATE TABLE IF NOT EXISTS `dataset` (
  `DS_ID` int(11) NOT NULL AUTO_INCREMENT,
  `Age` int(11) NOT NULL,
  `Glucose` int(11) NOT NULL,
  `BloodPressure` int(11) NOT NULL,
  `SkinThickness` int(11) NOT NULL,
  `Insulin` int(11) NOT NULL,
  `BMI` int(11) NOT NULL,
  `DiabetesPedigreeFunction` int(11) NOT NULL,
  `Pregnancies` int(11) NOT NULL,
  PRIMARY KEY (`DS_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'mainapp', 'user_details'),
(8, 'adminapp', 'dataset'),
(9, 'adminapp', 'upload_dataset_model'),
(10, 'userapp', 'dataset'),
(11, 'userapp', 'feedback'),
(12, 'adminapp', 'ada_algo'),
(13, 'adminapp', 'all_users_model'),
(14, 'adminapp', 'dt_algo'),
(15, 'adminapp', 'gd_algo'),
(16, 'adminapp', 'knn_algo'),
(17, 'adminapp', 'logistic'),
(18, 'adminapp', 'randomforest'),
(19, 'adminapp', 'svm_algo'),
(20, 'adminapp', 'xg_algo'),
(21, 'mainapp', 'last_login'),
(22, 'mainapp', 'predict_details');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-11-10 11:41:55.352541'),
(2, 'auth', '0001_initial', '2023-11-10 11:41:56.033676'),
(3, 'admin', '0001_initial', '2023-11-10 11:41:56.500425'),
(4, 'admin', '0002_logentry_remove_auto_add', '2023-11-10 11:41:56.516047'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-11-10 11:41:56.540016'),
(6, 'contenttypes', '0002_remove_content_type_name', '2023-11-10 11:41:56.647832'),
(7, 'auth', '0002_alter_permission_name_max_length', '2023-11-10 11:41:56.693796'),
(8, 'auth', '0003_alter_user_email_max_length', '2023-11-10 11:41:56.748593'),
(9, 'auth', '0004_alter_user_username_opts', '2023-11-10 11:41:56.775088'),
(10, 'auth', '0005_alter_user_last_login_null', '2023-11-10 11:41:56.826899'),
(11, 'auth', '0006_require_contenttypes_0002', '2023-11-10 11:41:56.826899'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2023-11-10 11:41:56.847720'),
(13, 'auth', '0008_alter_user_username_max_length', '2023-11-10 11:41:56.904380'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2023-11-10 11:41:56.944799'),
(15, 'auth', '0010_alter_group_name_max_length', '2023-11-10 11:41:57.008048'),
(16, 'auth', '0011_update_proxy_permissions', '2023-11-10 11:41:57.008048'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2023-11-10 11:41:57.073828'),
(18, 'mainapp', '0001_initial', '2023-11-10 11:41:57.093708'),
(19, 'sessions', '0001_initial', '2023-11-10 11:41:57.249861'),
(20, 'adminapp', '0001_initial', '2023-11-14 06:51:26.005058'),
(21, 'userapp', '0001_initial', '2023-11-14 08:02:02.970374'),
(22, 'adminapp', '0002_ada_algo_all_users_model_dt_algo_gd_algo_knn_algo_and_more', '2023-11-14 11:31:11.544096'),
(23, 'mainapp', '0002_last_login_predict_details', '2023-11-15 07:47:58.204774'),
(24, 'mainapp', '0003_user_details_message', '2023-11-15 10:01:52.400275');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('avqjip11hza65al9i6lh9thocttwkchk', 'eyJFbWFpbCI6InBwcmFzaGFudGhpMTY5QGdtYWlsLmNvbSIsIlVzZXJfaWQiOjN9:1r1kFS:eYGdnEBRAYgBsc_jw2s9z5Y9hNcnRyZvZFtIpd4_zyc', '2023-11-25 09:25:50.735561'),
('0btv7ju6726swuoak8gxktkmai8xiei4', 'eyJVc2VyX2lkIjozfQ:1r2nKy:mykuB-dUyT7zYqOBNXE84BijGFjJmePAPfvR-zwJN-0', '2023-11-28 06:55:52.129265'),
('kdsxdudfkv1pvutrqbxn8leipdqgib9m', 'eyJFbWFpbCI6InByYXZlZW5sdWNreTMyMkBnbWFpbC5jb20iLCJVc2VyX2lkIjo3fQ:1r3Cyy:59G2VhM1ZkVWMyLvludDvN1GH3ZZH0OG0QJFQkl79cw', '2023-11-29 10:18:52.531037'),
('6rrg3zrvpvyauh54nzsg5td7c4p14rlw', 'eyJVc2VyX2lkIjo1fQ:1r5i4p:3H74jG9g-kRz2-q6XHgH9701IzwAZ8Vfxc8zKn4mHcg', '2023-12-06 07:55:15.895326'),
('4qfh4egcyzz1p5q87r4unm2rkpa5b6yv', 'eyJVc2VyX2lkIjo1fQ:1r5iN4:3ZxdyK6yu0XpuTLmI5aBHj5n1Rs-PfKR8sXXCc_TmN0', '2023-12-06 08:14:06.447265'),
('cq1iji0vuzyj7qxogvku5368vflibqrl', 'eyJVc2VyX2lkIjo1fQ:1r5ij4:saMxKgXhrgvFkUxKjCf3U2bK2Z0ybyOuA2JwcfPcMLk', '2023-12-06 08:36:50.019941'),
('dzjsrl9prwu1r4lwlhgv2p4vepkb2q7k', 'eyJVc2VyX2lkIjo1LCJFbWFpbCI6InByYXZlZW5sdWNreTMyMkBnbWFpbC5jb20ifQ:1r5k6M:lM7auGCyqSajvA_rhBlM8XnBBDuNePaRBLJBwa98H3U', '2023-12-06 10:04:58.058524');

-- --------------------------------------------------------

--
-- Table structure for table `dt_algo`
--

DROP TABLE IF EXISTS `dt_algo`;
CREATE TABLE IF NOT EXISTS `dt_algo` (
  `DT_ID` int(11) NOT NULL AUTO_INCREMENT,
  `Accuracy` longtext NOT NULL,
  `Precession` longtext NOT NULL,
  `F1_Score` longtext NOT NULL,
  `Recall` longtext NOT NULL,
  `Name` longtext NOT NULL,
  PRIMARY KEY (`DT_ID`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dt_algo`
--

INSERT INTO `dt_algo` (`DT_ID`, `Accuracy`, `Precession`, `F1_Score`, `Recall`, `Name`) VALUES
(1, '99.71', '99.71', '99.71', '99.71', 'Decision Tree Algorithm'),
(2, '99.35', '99.35', '99.35', '99.36', 'Decision Tree Algorithm'),
(3, '99.78', '99.78', '99.78', '99.79', 'Decision Tree Algorithm'),
(4, '99.78', '99.78', '99.78', '99.79', 'Decision Tree Algorithm');

-- --------------------------------------------------------

--
-- Table structure for table `feedback_details`
--

DROP TABLE IF EXISTS `feedback_details`;
CREATE TABLE IF NOT EXISTS `feedback_details` (
  `Feed_id` int(11) NOT NULL AUTO_INCREMENT,
  `Rating` varchar(100) DEFAULT NULL,
  `Review` varchar(225) DEFAULT NULL,
  `Sentiment` varchar(100) DEFAULT NULL,
  `datetime` datetime(6) NOT NULL,
  `Reviewer_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`Feed_id`),
  KEY `feedback_details_Reviewer_id_13cf49be` (`Reviewer_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `feedback_details`
--

INSERT INTO `feedback_details` (`Feed_id`, `Rating`, `Review`, `Sentiment`, `datetime`, `Reviewer_id`) VALUES
(9, '3', 'Good', 'positive', '2023-11-22 09:46:12.405648', 8),
(8, '4', 'Good', 'positive', '2023-11-15 09:07:40.277596', 5),
(7, '1', 'very bad', 'negative', '2023-11-14 08:14:37.700865', 5),
(6, '2', 'bad', 'negative', '2023-11-14 08:14:11.160716', 5);

-- --------------------------------------------------------

--
-- Table structure for table `gd_algo`
--

DROP TABLE IF EXISTS `gd_algo`;
CREATE TABLE IF NOT EXISTS `gd_algo` (
  `GD_ID` int(11) NOT NULL AUTO_INCREMENT,
  `Accuracy` longtext NOT NULL,
  `Precession` longtext NOT NULL,
  `F1_Score` longtext NOT NULL,
  `Recall` longtext NOT NULL,
  `Name` longtext NOT NULL,
  PRIMARY KEY (`GD_ID`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `gd_algo`
--

INSERT INTO `gd_algo` (`GD_ID`, `Accuracy`, `Precession`, `F1_Score`, `Recall`, `Name`) VALUES
(1, '99.64', '99.64', '99.64', '99.64', 'XG Boost Algorithm'),
(2, '99.78', '99.78', '99.79', '99.79', 'XG Boost Algorithm'),
(3, '99.78', '99.78', '99.79', '99.79', 'XG Boost Algorithm'),
(4, '99.43', '99.43', '99.42', '99.42', 'XG Boost Algorithm');

-- --------------------------------------------------------

--
-- Table structure for table `knn_algo`
--

DROP TABLE IF EXISTS `knn_algo`;
CREATE TABLE IF NOT EXISTS `knn_algo` (
  `KNN_ID` int(11) NOT NULL AUTO_INCREMENT,
  `Accuracy` longtext NOT NULL,
  `Precession` longtext NOT NULL,
  `F1_Score` longtext NOT NULL,
  `Recall` longtext NOT NULL,
  `Name` longtext NOT NULL,
  PRIMARY KEY (`KNN_ID`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `knn_algo`
--

INSERT INTO `knn_algo` (`KNN_ID`, `Accuracy`, `Precession`, `F1_Score`, `Recall`, `Name`) VALUES
(1, '91.53', '91.39', '91.9', '91.9', 'ADA Boost Algorithm'),
(2, '91.67', '91.51', '92.15', '92.15', 'ADA Boost Algorithm'),
(3, '90.74', '90.61', '91.05', '91.05', 'ADA Boost Algorithm'),
(4, '91.31', '91.16', '91.72', '91.72', 'ADA Boost Algorithm'),
(5, '90.67', '90.57', '90.82', '90.82', 'ADA Boost Algorithm');

-- --------------------------------------------------------

--
-- Table structure for table `last_login`
--

DROP TABLE IF EXISTS `last_login`;
CREATE TABLE IF NOT EXISTS `last_login` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Login_Time` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `logistic`
--

DROP TABLE IF EXISTS `logistic`;
CREATE TABLE IF NOT EXISTS `logistic` (
  `Logistic_ID` int(11) NOT NULL AUTO_INCREMENT,
  `Accuracy` longtext NOT NULL,
  `Precession` longtext NOT NULL,
  `F1_Score` longtext NOT NULL,
  `Recall` longtext NOT NULL,
  `Name` longtext NOT NULL,
  PRIMARY KEY (`Logistic_ID`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `logistic`
--

INSERT INTO `logistic` (`Logistic_ID`, `Accuracy`, `Precession`, `F1_Score`, `Recall`, `Name`) VALUES
(1, '98.64', '98.6', '98.69', '98.69', 'ADA Boost Algorithm'),
(2, '98.28', '98.24', '98.33', '98.33', 'ADA Boost Algorithm'),
(3, '98.28', '98.25', '98.31', '98.31', 'ADA Boost Algorithm'),
(4, '97.77', '97.75', '97.81', '97.81', 'ADA Boost Algorithm'),
(5, '97.99', '97.97', '98.0', '98.0', 'ADA Boost Algorithm'),
(6, '98.56', '98.52', '98.63', '98.63', 'ADA Boost Algorithm'),
(7, '97.99', '97.96', '98.02', '98.02', 'ADA Boost Algorithm');

-- --------------------------------------------------------

--
-- Table structure for table `predict_detail`
--

DROP TABLE IF EXISTS `predict_detail`;
CREATE TABLE IF NOT EXISTS `predict_detail` (
  `predict_id` int(11) NOT NULL AUTO_INCREMENT,
  `Field_1` varchar(60) DEFAULT NULL,
  `Field_2` varchar(60) DEFAULT NULL,
  `Field_3` varchar(60) DEFAULT NULL,
  `Field_4` varchar(60) DEFAULT NULL,
  `Field_5` varchar(60) DEFAULT NULL,
  `Field_6` varchar(60) DEFAULT NULL,
  `Field_7` varchar(60) DEFAULT NULL,
  `Field_8` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`predict_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `randomforest`
--

DROP TABLE IF EXISTS `randomforest`;
CREATE TABLE IF NOT EXISTS `randomforest` (
  `Random_ID` int(11) NOT NULL AUTO_INCREMENT,
  `Accuracy` longtext NOT NULL,
  `Precession` longtext NOT NULL,
  `F1_Score` longtext NOT NULL,
  `Recall` longtext NOT NULL,
  `Name` longtext NOT NULL,
  PRIMARY KEY (`Random_ID`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `randomforest`
--

INSERT INTO `randomforest` (`Random_ID`, `Accuracy`, `Precession`, `F1_Score`, `Recall`, `Name`) VALUES
(1, '99.64', '99.63', '99.65', '99.65', 'XG Boost Algorithm'),
(2, '99.78', '99.78', '99.79', '99.79', 'XG Boost Algorithm'),
(3, '99.71', '99.71', '99.71', '99.71', 'XG Boost Algorithm'),
(4, '99.78', '99.78', '99.79', '99.79', 'XG Boost Algorithm');

-- --------------------------------------------------------

--
-- Table structure for table `sxm_algo`
--

DROP TABLE IF EXISTS `sxm_algo`;
CREATE TABLE IF NOT EXISTS `sxm_algo` (
  `SVM_ID` int(11) NOT NULL AUTO_INCREMENT,
  `Accuracy` longtext NOT NULL,
  `Precession` longtext NOT NULL,
  `F1_Score` longtext NOT NULL,
  `Recall` longtext NOT NULL,
  `Name` longtext NOT NULL,
  PRIMARY KEY (`SVM_ID`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sxm_algo`
--

INSERT INTO `sxm_algo` (`SVM_ID`, `Accuracy`, `Precession`, `F1_Score`, `Recall`, `Name`) VALUES
(1, '99.5', '99.49', '99.5', '99.5', 'XG Boost Algorithm'),
(2, '99.5', '99.49', '99.5', '99.5', 'XG Boost Algorithm'),
(3, '99.35', '99.35', '99.36', '99.36', 'XG Boost Algorithm'),
(4, '99.71', '99.7', '99.72', '99.72', 'XG Boost Algorithm'),
(5, '99.64', '99.63', '99.65', '99.65', 'XG Boost Algorithm'),
(6, '99.64', '99.64', '99.64', '99.64', 'XG Boost Algorithm');

-- --------------------------------------------------------

--
-- Table structure for table `upload`
--

DROP TABLE IF EXISTS `upload`;
CREATE TABLE IF NOT EXISTS `upload` (
  `Data_id` int(11) NOT NULL AUTO_INCREMENT,
  `Image` varchar(100) NOT NULL,
  PRIMARY KEY (`Data_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `upload_dataset`
--

DROP TABLE IF EXISTS `upload_dataset`;
CREATE TABLE IF NOT EXISTS `upload_dataset` (
  `User_id` int(11) NOT NULL AUTO_INCREMENT,
  `Dataset` varchar(100) DEFAULT NULL,
  `File_size` varchar(100) NOT NULL,
  `Date_Time` datetime(6) NOT NULL,
  PRIMARY KEY (`User_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `upload_dataset`
--

INSERT INTO `upload_dataset` (`User_id`, `Dataset`, `File_size`, `Date_Time`) VALUES
(5, 'thyroid_clean_b0X2FE9.csv', '267.2939453125 kb', '2023-11-15 09:17:31.677259');

-- --------------------------------------------------------

--
-- Table structure for table `user_detail`
--

DROP TABLE IF EXISTS `user_detail`;
CREATE TABLE IF NOT EXISTS `user_detail` (
  `User_id` int(11) NOT NULL AUTO_INCREMENT,
  `Full_name` varchar(100) NOT NULL,
  `Image` varchar(100) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Address` varchar(200) DEFAULT NULL,
  `Age` int(11) DEFAULT NULL,
  `Phone_Number` varchar(10) DEFAULT NULL,
  `Password` varchar(15) DEFAULT NULL,
  `Date_Time` datetime(6) DEFAULT NULL,
  `User_Status` varchar(50) DEFAULT NULL,
  `Otp_Num` int(11) DEFAULT NULL,
  `Otp_Status` varchar(60) DEFAULT NULL,
  `Last_Login_Time` time(6) DEFAULT NULL,
  `Last_Login_Date` date DEFAULT NULL,
  `No_Of_Times_Login` int(11) DEFAULT NULL,
  `Message` longtext DEFAULT NULL,
  PRIMARY KEY (`User_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_detail`
--

INSERT INTO `user_detail` (`User_id`, `Full_name`, `Image`, `Email`, `Address`, `Age`, `Phone_Number`, `Password`, `Date_Time`, `User_Status`, `Otp_Num`, `Otp_Status`, `Last_Login_Time`, `Last_Login_Date`, `No_Of_Times_Login`, `Message`) VALUES
(5, 'prashanthi', 'images/rose_BLSRSN1.jpg', 'pprashanthi169@gmail.com', 'hyderabad', 25, '9949803766', 'Amma@123', '2023-11-22 10:06:53.469185', 'accepted', 5398, 'verified', '15:36:53.000000', '2023-11-22', 12, 'Good'),
(9, 'praveen', 'images/rose_e0pTRQS.jpg', 'praveenlucky322@gmail.com', 'khammam', 26, '7989373610', 'Kutty@123', '2023-11-22 10:02:33.316173', 'pending', 6309, 'pending', NULL, '2023-11-22', 0, NULL),
(8, 'prashanthi', 'images/pink_VAfeL87.jpg', 'prashanthi3766@gmail.com', '', 25, '9949803766', 'Amma@123', '2023-11-22 09:46:25.865547', 'accepted', 4094, 'verified', '15:16:25.000000', '2023-11-22', 1, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `xg_algo`
--

DROP TABLE IF EXISTS `xg_algo`;
CREATE TABLE IF NOT EXISTS `xg_algo` (
  `XG_ID` int(11) NOT NULL AUTO_INCREMENT,
  `Accuracy` longtext NOT NULL,
  `Precession` longtext NOT NULL,
  `F1_Score` longtext NOT NULL,
  `Recall` longtext NOT NULL,
  `Name` longtext NOT NULL,
  PRIMARY KEY (`XG_ID`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `xg_algo`
--

INSERT INTO `xg_algo` (`XG_ID`, `Accuracy`, `Precession`, `F1_Score`, `Recall`, `Name`) VALUES
(1, '99.78', '99.78', '99.79', '99.79', 'XG Boost Algorithm'),
(2, '99.57', '99.56', '99.58', '99.58', 'XG Boost Algorithm'),
(3, '99.71', '99.71', '99.72', '99.72', 'XG Boost Algorithm'),
(4, '99.78', '99.78', '99.79', '99.79', 'XG Boost Algorithm'),
(5, '99.5', '99.5', '99.49', '99.49', 'XG Boost Algorithm'),
(6, '99.78', '99.79', '99.78', '99.78', 'XG Boost Algorithm'),
(7, '99.78', '99.79', '99.78', '99.78', 'XG Boost Algorithm'),
(8, '99.86', '99.86', '99.86', '99.86', 'XG Boost Algorithm'),
(9, '99.78', '99.79', '99.78', '99.78', 'XG Boost Algorithm'),
(10, '99.71', '99.72', '99.71', '99.71', 'XG Boost Algorithm'),
(11, '99.86', '99.86', '99.86', '99.86', 'XG Boost Algorithm'),
(12, '99.86', '99.86', '99.86', '99.86', 'XG Boost Algorithm'),
(13, '99.78', '99.78', '99.79', '99.79', 'XG Boost Algorithm');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
