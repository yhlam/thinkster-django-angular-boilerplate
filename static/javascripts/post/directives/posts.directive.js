/**
 * Posts
 * @namespace thinkster.post.directives
 */
(function() {
  'use strict';

  angular
    .module('thinkster.post.directives')
    .directive('posts', posts);

  /**
   * @namespace Posts
   */
  function posts() {
    /**
     * @name directive
     * @desc The directive to be returned
     * @memberOf thinkster.post.directives.Posts
     */
    var directive = {
      controller: 'PostsController',
      controllerAs: 'vm',
      restrict: 'E',
      scope: {
        posts: '='
      },
      templateUrl: '/static/templates/post/posts.html'
    };

    return directive;
  }
})();
