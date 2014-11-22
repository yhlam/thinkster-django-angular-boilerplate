/**
 * Post
 * @namespace thinkster.post.directives
 */
(function() {
  'use strict';

  angular
    .module('thinkster.post.directives')
    .directive('post', post);

  /**
   * @namespace Post
   */
  function post() {
    /**
     * @name directive
     * @desc The directive to be returned
     * @memberOf thinkster.post.directives.Post
     */
    var directive = {
      restrict: 'E',
      scope: {
        post: '='
      },
      templateUrl: '/static/templates/post/post.html'
    };

    return directive;
  }
})();
