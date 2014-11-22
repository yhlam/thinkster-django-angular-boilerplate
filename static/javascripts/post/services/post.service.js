(function() {
  'use strict';

  angular
    .module('thinkster.post.services')
    .factory('Post', Post);

  Post.$inject = ['$http'];

  function Post($http) {
    var Post = {
      all: all,
      create: create,
      get: get
    }

    return Post;

    ////////////////////

    /**
     * @name all
     * @desc Get all posts
     * @returns {Promise}
     * @memberOf thinkster.post.services.Post
     */
    function all() {
      return $http.get('/api/v1/post/');
    }

    /**
     * @name create
     * @desc Create a new post
     * @param {string} content The content of the new post
     * @returns {Promise}
     * @memberOf thinkster.post.services.Post
     */
    function create(content) {
      return $http.post('/api/v1/post/', {content: content});
    }

    /**
     * @name get
     * @desc Get the posts of a given user
     * @param {string} username The username to get posts for
     * @returns {Promise}
     * @memberOf thinkster.post.services.Post
     */
    function get(username) {
      return $http.get('/api/v1/account/' + username + '/post/');
    }
  }
})();
