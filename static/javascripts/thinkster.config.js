(function() {
  'use strict';

  angular
    .module('thinkster.config')
    .config(config);

  config.$inject = ['$locationProvider', '$httpProvider', 'jwtInterceptorProvider'];

  /**
   * @name config
   * @desc Enable HTML5 routing, CSRF and JWT
   */
  function config($locationProvider, $httpProvider, jwtInterceptorProvider) {
    html5Mode($locationProvider);
    csrf($httpProvider);
    jwt(jwtInterceptorProvider);

    function html5Mode($locationProvider) {
      $locationProvider.html5Mode(true);
      $locationProvider.hashPrefix('!');
    }

    function csrf($httpProvider) {
      $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
      $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    }

    function jwt(jwtInterceptorProvider) {
      jwtInterceptorProvider.tokenGetter = function() {
        return localStorage.getItem('id_token');
      }
      jwtInterceptorProvider.authPrefix = 'JWT ';
      $httpProvider.interceptors.push('jwtInterceptor');
    }
  }
})();
