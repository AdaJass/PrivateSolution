CREATE DATABASE IF NOT EXISTS `Currency` DEFAULT CHARACTER SET utf8;
USE Currency;
CREATE TABLE IF NOT EXISTS `atos` (
  `DATE` datetime NOT NULL,
  `EURUSD` float unsigned zerofill DEFAULT NULL,
  `GBPUSD` float unsigned zerofill DEFAULT NULL,
  `USDJPY` float unsigned zerofill DEFAULT NULL,
  `AUDUSD` float unsigned zerofill DEFAULT NULL,
  `XAUUSD` float unsigned zerofill DEFAULT NULL,
  `XAGUSD` float unsigned zerofill DEFAULT NULL,
  `OIL` float unsigned zerofill DEFAULT NULL,
  `HKG50` float unsigned zerofill DEFAULT NULL,
  `US30` float unsigned zerofill DEFAULT NULL,
  PRIMARY KEY (`DATE`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `xm` (
  `DATE` datetime NOT NULL,
  `EURUSD` float unsigned zerofill DEFAULT NULL,
  `GBPUSD` float unsigned zerofill DEFAULT NULL,
  `USDJPY` float unsigned zerofill DEFAULT NULL,
  `XAUUSD` float unsigned zerofill DEFAULT NULL,
  `XAGUSD` float unsigned zerofill DEFAULT NULL,
  `OIL` float unsigned zerofill DEFAULT NULL,
  `US30` float unsigned zerofill DEFAULT NULL,
  `GER30` float unsigned zerofill DEFAULT NULL,
  `JP225` float unsigned zerofill DEFAULT NULL,
  `EURJPY` float unsigned zerofill DEFAULT NULL,
  `GBPJPY` float unsigned zerofill DEFAULT NULL,
  PRIMARY KEY (`DATE`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

