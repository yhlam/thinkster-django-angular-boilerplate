(function() {
  'use strict';

  angular
    .module('thinkster', [
      'thinkster.config',
      'thinkster.routes',
      'thinkster.authentication',
      'thinkster.layout',
      'thinkster.post',
      'thinkster.util',
    ]);

  angular
    .module('thinkster.routes', ['ngRoute']);

  angular
    .module('thinkster.config', ['angular-jwt']);
})();
