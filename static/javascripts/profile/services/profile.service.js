/**
 * Profile
 * @namespace thinkster.profile.services
 */
(function () {
  'use strict';

  angular
    .module('thinkster.profile.services')
    .factory('Profile', Profile);

  Profile.$inject = ['$http'];

  /**
   * @namespace Profile
   */
  function Profile($http) {
    /**
     * @name Profile
     * @desc The factory to be returned
     * @memberOf thinkster.profile.services.Profile
     */
    var Profile = {
      destroy: destroy,
      get: get,
      update: update
    }

    return Profile;

    ////////////////////

    /**
     * @name destory
     * @desc Destroys the given profile
     * @param {Object} profile The profile to be destoryed
     * @returns {Promise}
     * @memberOf thinkster.profile.services.Profile
     */
    function destroy(profile) {
      return $http.delete('/api/v1/account/' + profile.username + '/');
    }

    /**
     * @name get
     * @desc Gets the profile for user with username `username`
     * @param {string} username The username of the user to fetch
     * @returns {Promise}
     * @memberOf thinkster.profile.services.Profile
     */
    function get(username) {
      return $http.get('/api/v1/account/' + username + '/');
    }

    /**
     * @name update
     * @desc Update the given profile
     * @param {Object} profile The profile to be updated
     * @returns {Promise}
     * @memberOf thinkster.profile.services.Profile
     */
    function update(profile) {
      return $http.put('/api/v1/account/' + profile.username + '/', profile);
    }
  }
})();
