-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 28, 2020 at 06:12 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.2.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `grocery`
--

-- --------------------------------------------------------

--
-- Table structure for table `kriyana`
--

CREATE TABLE `kriyana` (
  `id` int(11) NOT NULL,
  `product` varchar(50) NOT NULL,
  `quantity` int(11) NOT NULL,
  `price` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `kriyana`
--

INSERT INTO `kriyana` (`id`, `product`, `quantity`, `price`) VALUES
(1, 'maggi', 100, 10),
(2, 'meshwak', 41, 92),
(3, 'harpic', 55, 62),
(5, 'paste', 50, 100),
(25, 'lux', 100, 56),
(87, 'sun silk', 100, 2),
(101, 'dabur honey', 19, 45),
(102, 'cholle', 1, 60),
(103, 'chocolate', 52, 98),
(108, 'haldi', 56, 45),
(110, 'paste', 45, 100),
(111, 'soap', 55, 147);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `kriyana`
--
ALTER TABLE `kriyana`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
