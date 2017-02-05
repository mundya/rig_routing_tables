#include "tests.h"


int main(void)
{
  int n_failed;

  Suite *s_bitset = bitset_suite();
  SRunner *sr = srunner_create(s_bitset);

  Suite *s_routing_table = routing_table_suite();
  srunner_add_suite(sr, s_routing_table);

  Suite *s_merge = merge_suite();
  srunner_add_suite(sr, s_merge);

  Suite *s_aliases = aliases_suite();
  srunner_add_suite(sr, s_aliases);

  Suite *s_oc = ordered_covering_suite();
  srunner_add_suite(sr, s_oc);

  Suite *s_mtrie = mtrie_suite();
  srunner_add_suite(sr, s_mtrie);

  Suite *s_rdr = remove_default_suite();
  srunner_add_suite(sr, s_rdr);

  // Run the tests
  srunner_run_all(sr, CK_NORMAL);

  n_failed = srunner_ntests_failed(sr);
  srunner_free(sr);

  return (n_failed == 0) ? EXIT_SUCCESS : EXIT_FAILURE;
}
