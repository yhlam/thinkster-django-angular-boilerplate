/**
 * Authentication
 * @namespace thinkster.authentication.services
 */
(function() {
  'use strict';

  angular
    .module('thinkster.authentication.services')
    .factory('Authentication', Authentication);

  Authentication.$inject = ['$cookies', '$http', '$window'];

  /**
   * @namespace Authentication
   * @returns {Factory}
   */
  function Authentication($cookies, $http, $window) {
    /**
    * @name Authentication
    * @desc The Factory to be returned
    */
    var Authentication = {
      getAuthenticatedAccount: getAuthenticatedAccount,
      isAuthenticated: isAuthenticated,
      login: login,
      logout: logout,
      register: register,
      setAuthenticatedAccount: setAuthenticatedAccount,
    };

    return Authentication;

    ////////////////////

    /**
     * @name login
     * @desc Try to log in with email `email` and password `password`
     * @param {string} email The email entered by the user
     * @param {string} password The password entered by the user
     * @returns {Promise}
     * @memberOf thinkster.authentication.services.Authentication
     */
    function login(email, password) {
      return $http.post('/api-token-auth/', {
        email: email,
        password: password
      })
        .then(storeToken)
        .then(getCurrentUser)
        .then(setAuthenticatedAccount);

      function storeToken(data, status, headers, config) {
        $window.localStorage.setItem('id_token', data.data.token);
      }

      function loginError(data, status, headers, config) {
        return $q.reject('Invalid email or password');
      }

      function getCurrentUser() {
        return $http.get('/api/v1/account/me/');
      }

      function setAuthenticatedAccount(data, status, headers, config) {
        Authentication.setAuthenticatedAccount(data.data);
      }
    }

    /**
     * @name logout
     * @desc Try to log the user out
     * @returns {undefined}
     * @memberOf thinkster.authentication.services.Authentication
     */
    function logout() {
      $window.localStorage.removeItem('id_token');
      delete $cookies.authenticatedAccount;
    }

    /**
     * @name registry
     * @desc Try to register a new user
     * @param {string} username The username entered by the user
     * @param {string} password The password entered by the user
     * @param {string} confirmPassword The confirm password entered by the user
     * @param {string} email The email entered by the user
     * @returns {Promise}
     * @memberOf thinkster.authentication.services.Authentication
     */
    function register(username, password, confirmPassword, email) {
      return $http.post('/api/v1/account/', {
        username: username,
        password: password,
        confirm_password: confirmPassword,
        email: email
      });
    }

    /**
     * @name getAuthenticatedAccount
     * @desc Return the currently authenticated account
     * @returns {object|undefined} Account if authenticated, else undefined
     * @memberOf thinkster.authentication.services.Authentication
     */
    function getAuthenticatedAccount() {
      if(!$cookies.authenticatedAccount) {
        return;
      }

      return JSON.parse($cookies.authenticatedAccount);
    }

    /**
     * @name isAuthenticated
     * @desc Check if the current user is authenticated
     * @returns {boolean} True if user is authenticated, else false
     * @memberOf thinkster.authentication.services.Authentication
     */
    function isAuthenticated() {
      return !!$cookies.authenticatedAccount;
    }

    /**
     * @name setAuthenticatedAccount
     * @desc Stringify the account object and store it in a cookie
     * @param {object} account the Account object to be stored
     * @returns {object|undefined} Account if authenticated, else undefined
     * @memberOf thinkster.authentication.services.Authentication
     */
    function setAuthenticatedAccount(account) {
      return $cookies.authenticatedAccount = JSON.stringify(account);
    }
  }

})();
