(function() {
  'use strict';

  angular
    .module('thinkster.config')
    .config(config);

  config.$inject = ['$locationProvider', '$httpProvider'];

  /**
   * @name config
   * @desc Enable HTML5 routing and CSRF
   */
  function config($locationProvider, $httpProvider) {
    html5Mode($locationProvider);
    csrf($httpProvider);

    function html5Mode($locationProvider) {
      $locationProvider.html5Mode(true);
      $locationProvider.hashPrefix('!');
    }

    function csrf($httpProvider) {
      $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
      $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    }
  }
})();
